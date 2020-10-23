# drf_best_enum_serializer

Some time ago, I ran into the problem of serializing a ChoiceField in Django Restframework.
I needed the field to be able to correctly accept and process both: the key and the value for the ChoiceField, as well as the enum or the ChoiceField in the case of POST and PUT requests, and also return the ChoiceField field as an object containing {"value": value, "display_name": display_name} on GET.

I had to redefine the behavior a little and create my own. Now Django serializers work as I need :)
