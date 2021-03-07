from django.db import models


class UserDocuments(models.Model):
    # user_details = models.ForeignKey(UserDetails, on_delete=models.SET_NULL, null=True, blank=True)
    # related_user_details = models.ForeignKey(RelatedUserDetails, on_delete=models.SET_NULL, null=True, blank=True)
    doc_name = models.CharField(max_length=150, default='', blank=True)
    doc = models.FileField(blank=False, null=True)
    doc_link = models.CharField(max_length=150, default='', blank=True)
    doc_type = models.CharField(max_length=50, default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def str(self):
        return str(self.id)
