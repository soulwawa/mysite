from django.utils.log import AdminEmailHandler
from django.core.mail import EmailMultiAlternatives


class SendgridAdminEmailHandler(AdminEmailHandler):

    def send_mail(self, subject, message, *args, **kwargs):
        try:
            if kwargs.get('html_message') is not None:
                message_content = kwargs['html_message']
            else:
                message_content = message

            # send_mail(admin_mail, subject, message_content, message)
            email = EmailMultiAlternatives(
                subject=subject,
                body=message_content,
                from_email='soulwawa85@gmail.com',
                to=['soulwawa85@gmail.com'])
            email.send()
        except:
            pass