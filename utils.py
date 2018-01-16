from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

def sendEmail(txt='',html='',data={},title='',to=[]):
    emailTxt = get_template(txt)
    emailHtml = get_template(html)
    textContent = emailTxt.render(data)
    htmlContent = emailHtml.render(data)
    msg = EmailMultiAlternatives(title,textContent,'hua-ting.yao@u-psud.fr',to)
    msg.attach_alternative(htmlContent, "text/html")
    msg.send()
    return True

