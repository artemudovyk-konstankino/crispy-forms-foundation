"""
Foundation grid layout objects
"""
from django.conf import settings
from django.template import Context
from django.template.loader import render_to_string

from crispy_forms.utils import render_field
from crispy_forms import layout as crispy_forms_layout
from crispy_forms import bootstrap as crispy_forms_bootstrap

from crispy_forms_foundation.layout.base import Div

TEMPLATE_PACK = getattr(settings, 'CRISPY_TEMPLATE_PACK', 'foundation-5')

class Row(Div):
    """
    It wraps fields in a div whose default class is ``row``. Example:

    .. sourcecode:: python

        Row('form_field_1', 'form_field_2', 'form_field_3')

    Act as a div container row, it will embed its items in a div like that:

    .. sourcecode:: html

        <div class"row">Your stuff</div>
    """
    css_class = 'row'

class RowFluid(Row):
    """
    It wraps fields in a div whose default class is "row row-fluid". Example:

    .. sourcecode:: python

        RowFluid('form_field_1', 'form_field_2', 'form_field_3')

    It has a same behaviour than *Row* but add a CSS class "row-fluid" that you can use to have top level row that take all the container width. You have to put the CSS for this class to your CSS stylesheets. It will embed its items in a div like that:

    .. sourcecode:: html

        <div class"row row-fluid">Your stuff</div>

    The CSS to add should be something like that:

    .. sourcecode:: css

        .row-fluid {
            width: 100%;
            max-width: 100%;
            min-width: 100%;
        }
    """
    css_class = 'row row-fluid'


class Column(Div):
    """
    .. _Foundation Grid: http://foundation.zurb.com/docs/components/grid.html

    It wraps fields in a div. If not defined, CSS class will default to
    ``large-12 columns``. ``columns`` class is always appended, so you don't
    need to specify it.

    This is the column from the `Foundation Grid`_, all columns should be
    contained in a **Row** or a **RowFluid** and you will have to define the
    column type in the ``css_class`` attribute.

    Example:

    .. sourcecode:: python

        Column('form_field_1', 'form_field_2', css_class='small-12 large-6')

    Will render to something like that:

    .. sourcecode:: html

        <div class"small-12 large-6 columns">...</div>

    ``columns`` class is always appended, so you don't need to specify it.

    If not defined, ``css_class`` will default to ``large-12``.
    """
    css_class = 'columns'

    def __init__(self, field, *args, **kwargs):
        self.field = field
        if 'css_class' not in kwargs:
            kwargs['css_class'] = 'large-12'

        super(Column, self).__init__(field, *args, **kwargs)
