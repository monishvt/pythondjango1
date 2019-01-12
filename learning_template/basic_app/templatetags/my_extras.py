from django import template

register= template.Library()


@register.filter(name='cutit')
def cut(value,  arg):
	''' this cuts all values of arg from the string'''
	return value.replace(arg, '')

# register.filter('cutit', cut)