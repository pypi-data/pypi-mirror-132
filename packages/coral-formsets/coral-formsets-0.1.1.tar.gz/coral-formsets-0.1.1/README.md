# coral-formsets

Extensão para manipular o frontend usando Django [FormSets](https://docs.djangoproject.com/en/dev/topics/forms/formsets/).

Não tem dependência com outro framework/biblioteca javascript.

## Documentation

### Installation

Para instalar coral-formsets:

```shell
pip install coral-formsets
```

Adicione `coral_formsets` em `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # other apps
    "coral_formsets",
]
```

### Usage

No seu html adicione o `js` como no exemplo abaixo.  
Nesse exeplo `yourapp/form.html` é um arquivo referente ao template do seu form, isso garante mais clareza ao seu código:

```html
<!-- yourapp/form.html -->
<div data-form>
  <div style="display: none">{{ form.DELETE }}{{ form.id }}</div>
  {{ form.as_p }}
  <button data-delete>
    delete form
  </button>
</div>
```

```html
<!-- yourapp/view.html -->
{% load static coral_formset_tags %}
<!DOCTYPE html>
<html>
<body>
  <div data-formset>
    {% render_empty_form_template 'yourapp/form.html' formset as empty_form %}

    {{ formset.management_form }}

    <div data-body>
      {% for form in formset %}
        {% include 'yourapp/form.html' with form=form %}
      {% endfor %}
    </div>

    <button class="formset"
            data-empty-form="{{ empty_form }}"
            data-prefix="{{ formset.prefix }}">
      Add form
    </button>
  </div>

  <script src="{% static 'coral_formsets/js/FormSet.js' %}"></script>
  <script>
    document.querySelectorAll('.formset').forEach(el => {
      new window.coral.FormSet(el);
    });
  </script>
</body>
</html>
```

A templatetag `render_empty_form_template` irá transformar o seu `formset.empty_form` em texto, para depois fazer a inserção do novo form via javascript.
