"use strict"
{
  const GUID = Symbol("GUID");

  class FormSet {
    static _instances = new Map();

    static _genid() {
      return Math.random().toString(36).substr(2, 9);
    }

    static data(element) {
      return FormSet._instances.has(element[GUID]) && FormSet._instances.get(element[GUID]);
    }

    constructor(element, opts = {}) {
      this.opts = {
        insertIn: "beforeend",
        ...opts,
      }

      const instance = FormSet.data(element);
      if (instance instanceof FormSet) {
        throw new TypeError('The formset has already been instanced. Use the static method `FormSet.data(element)` to get the instance.');
      }

      this.validate();

      this._id = FormSet._genid();
      this.addbutton = element;
      this.container = this.addbutton.closest("[data-formset]");
      this.prefix = this.addbutton.getAttribute("data-prefix");
      this.body = this.container.querySelector("[data-body]");
      this.addbutton.addEventListener("click", this.addForm.bind(this));
      this.emptyForm = this.addbutton.dataset.emptyForm;

      const formsWithoutIds = this.container.querySelectorAll("[data-form]:not([data-form-id])");
      this.applyFormIds(formsWithoutIds);

      this.forms.forEach(form => this.applyDeleteHandle(form));

      this.toggleDeleteButtonVisibility();
      this.toggleAddButtonVisibility();
      this.toggleFormsVisibility();

      // Storage instance
      this.addbutton[GUID] = this._id;
      FormSet._instances.set(this.addbutton[GUID], this);
    }

    validate() {
      if (!["afterbegin", "beforeend"].includes(this.opts.insertIn)) {
        throw Error('insertIn só pode ter os valores beforeend|afterbegin.');
      }
    }

    updateElementIndex(el, prefix, newIdx) {
      const idRegex = new RegExp(`(${prefix}-(\\d+|__prefix__))`, "g");
      const replacement = `${prefix}-${newIdx}`;

      if (el.hasAttribute("for")) {
        const newAttr = el.getAttribute("for").replace(idRegex, replacement);
        el.setAttribute("for", newAttr);
      }

      if (el.id) {
        el.id = el.id.replace(idRegex, replacement);
      }
      if (el.name) {
        el.name = el.name.replace(idRegex, replacement);
      }
    }

    addForm(event) {
      event.preventDefault();

      if (!this.canAdd()) {
        alert(`Você só pode adicionar ${this.maxNumForms} formulário(s).`);
        return;
      }

      const idRegex = new RegExp(`(${this.prefix}-(\\d+|__prefix__))`, "g");
      const replacement = `${this.prefix}-${this.totalForms}`;

      const newForm = this.emptyForm.replace(idRegex, replacement);

      this.body.insertAdjacentHTML(this.opts.insertIn, newForm);
      let form = null;
      if (this.opts.insertIn === "beforeend") {
        form = this.body.lastElementChild;
      }
      else {
        form = this.body.firstElementChild;
      }

      this.applyFormIds([form]);
      this.applyDeleteHandle(form);
      this.totalForms++;
      this.toggleDeleteButtonVisibility();
      this.toggleAddButtonVisibility();

      const evt = new CustomEvent("formset:added", {
        detail: { prefix: this.prefix, formAdded: form }
      });
      document.dispatchEvent(evt);
    }

    deleteForm(event) {
      event.preventDefault();

      if (!this.canDelete()) {
        alert(`Você pode ter no mínimo ${this.minNumForms} formulário(s).`);
        return;
      }

      const form = event.target.closest("[data-form]");
      const id = form.querySelector("input[name$=-id]");
      const delCheck = form.querySelector("input[name$=-DELETE]");
      delCheck.checked = true;

      if (id.value === "") {
        form.remove();
        this.totalForms--;
      } else {
        this.hide(form);
        form.setAttribute("data-form-deleted", "");
      }

      this.forms.forEach((f, idx) => {
        f.querySelectorAll("*").forEach(el => {
          this.updateElementIndex(el, this.prefix, idx);
        })
      });

      this.toggleDeleteButtonVisibility();
      this.toggleAddButtonVisibility();

      // Dispatch the event
      const evt = new CustomEvent("formset:deleted", {
        detail: { prefix: this.prefix, formDeleted: form }
      });
      document.dispatchEvent(evt);
    }

    applyDeleteHandle(form) {
      const btnDelete = form.querySelector("[data-delete]");
      if (btnDelete !== null) {
        btnDelete.addEventListener("click", this.deleteForm.bind(this));
      }
    }

    toggleDeleteButtonVisibility() {
      if (this.canDelete()) {
        this.forms.forEach(f => this.show(f.querySelector("[data-delete]")));
      } else {
        this.forms.forEach(f => this.hide(f.querySelector("[data-delete]")));
      }
    }

    toggleAddButtonVisibility() {
      if (this.canAdd()) {
        this.show(this.addbutton);
      } else {
        this.hide(this.addbutton);
      }
    }

    toggleFormsVisibility() {
      this.forms.forEach(f => {
        const delCheck = f.querySelector("input[name$=-DELETE]");
        if (delCheck && delCheck.checked) {
          this.hide(f);
          f.setAttribute("data-form-deleted", "");
        }
      })
    }

    applyFormIds(forms) {
      forms.forEach(f => f.setAttribute('data-form-id', this._id));
    }

    hide(el) { el.style.display = "none" }

    show(el) { el.style.display = "" }

    canAdd() {
      return (this.maxNumForms - this.totalForms) > 0;
    }

    canDelete() {
      return (this.minNumForms - this.totalForms) < 0;
    }

    get visibleForms() {
      return this.container.querySelectorAll(`[data-form-id="${this._id}"]:not([data-form-deleted])`);
    }

    get forms() {
      return this.container.querySelectorAll(`[data-form-id="${this._id}"]`);
    }

    get totalForms() {
      return parseInt(this.container.querySelector(`#id_${this.prefix}-TOTAL_FORMS`).value);
    }

    set totalForms(value) {
      this.container.querySelector(`#id_${this.prefix}-TOTAL_FORMS`).value = value;
    }

    get minNumForms() {
      return parseInt(this.container.querySelector(`#id_${this.prefix}-MIN_NUM_FORMS`).value);
    }

    get maxNumForms() {
      return parseInt(this.container.querySelector(`#id_${this.prefix}-MAX_NUM_FORMS`).value);
    }
  }

  if (!window.coral) {
    window.coral = {};
  }
  window.coral.FormSet = FormSet;
}
