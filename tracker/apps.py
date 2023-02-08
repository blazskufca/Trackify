from django.apps import AppConfig


class TrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tracker'

    def ready(self):
        from scheduler import scheduler
        from django.contrib.auth.models import Group
        from django.conf import settings
        from django.db.models.signals import post_save
        import tracker.signals
        def add_to_default_group(sender, **kwargs):
            # Instance is the user model that was created
            user = kwargs.get('instance')
            # If the user was successfully created
            if kwargs.get('created'):
                # Get or create group called "default"
                group, ok =Group.objects.get_or_create('default')
                # Add the user to group
                group.user_set.add(user)
        scheduler.start()


