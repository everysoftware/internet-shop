import email

from app.core.config import cfg
from app.core.models import User


def thank_you(user: User) -> str:
    template = email.message.EmailMessage()
    template["Subject"] = "Добро пожаловать в наш интернет-магазин!"
    template["From"] = cfg.smtp.username
    template["To"] = user.email

    template.set_content(
        '<div style="font-family: Arial, sans-serif; color: #333;">'
        f'<h1 style="color: #48a999;">Здравствуйте, {user.first_name}!</h1>'
        "<p>Благодарим вас за регистрацию в нашем интернет-магазине. "
        "Мы рады приветствовать вас в нашем сообществе покупателей!</p>"
        "<p>С нашим магазином вы можете быть уверены, что ваши покупки будут быстрыми, удобными и безопасными.</p>"
        "<p>Если у вас возникнут вопросы или предложения, не стесняйтесь обращаться к нам.</p>"
        '<p style="color: #48a999;">С уважением,</p>'
        '<p style="color: #48a999;">Команда нашего интернет-магазина</p>'
        "</div>",
        subtype="html",
    )
    return template.as_string()
