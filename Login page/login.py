import requests
from ttkbootstrap import Frame as div
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import Personalization as per
from forgot_password import forgot_password


class gg(tb.Window):
    def __init__(self):
        super().__init__(themename="superhero")
        self.show_im = tb.ImageTk.PhotoImage(
            tb.Image.open("image\\show.png").resize((20, 20))
        )
        self.hide_im = tb.ImageTk.PhotoImage(
            tb.Image.open("image\\hide.png").resize((20, 20))
        )

        self.im = tb.ImageTk.PhotoImage(
            tb.Image.open("image\\im2.jpg").resize((560, 800))
        )
        self.Lim = tb.Label(image=self.im, padding=0)
        self.Lim.grid(row=0, column=0, padx=(0, 20))

        self.notebook = tb.Notebook(self, bootstyle=DARK, padding=0)
        self.notebook.grid(row=0, column=1, padx=(0, 10))
        # ======================================================login tab=================================================
        self.loginTab = tb.Frame(self.notebook)

        self.user_input = per.Entry_Placeholder(
            self.loginTab,
            placeholder="Username",
            width=25,
        )
        self.user_input.pack(padx=25, pady=30)

        self.passFrame = tb.Frame(self.loginTab)
        self.pass_input = per.Entry_Placeholder_password(
            self.passFrame,
            placeholder="Password",
            show_image="image/show.png",
            hide_image="image/hide.png",
        )
        self.passFrame.pack(padx=25, pady=30)

        self.forget_button = tb.Button(
            self.loginTab, text="Forget your Password?", bootstyle=(PRIMARY, LINK), command=lambda :forgot_password(self)
        )
        self.forget_button.pack()
        self.LoginB = tb.Button(self.loginTab, text="Login", command=self.login)
        self.LoginB.pack(padx=20, pady=25)

        self.login_status = tb.Label(self.loginTab, text="")
        self.login_status.pack()

        # ============================================================signup tab=================================================
        self.signupTab = tb.Frame(self.notebook)
        self.signup_user_input = per.Entry_Placeholder(
            self.signupTab,
            placeholder="Username",
            width=25,
        )
        self.signup_user_input.pack(padx=15, pady=20)

        self.signup_email_input = per.Entry_Placeholder(
            self.signupTab,
            placeholder="Email",
            width=25,
        )
        self.signup_email_input.pack(padx=15, pady=20)

        self.signup_passFrame1 = tb.Frame(self.signupTab)
        self.signup_pass_input1 = per.Entry_Placeholder_password(
            self.signup_passFrame1,
            placeholder="Password",
            show_image="image/show.png",
            hide_image="image/hide.png",
        )
        self.signup_passFrame1.pack(padx=15, pady=20)

        self.signup_passFrame2 = tb.Frame(self.signupTab)
        self.signup_pass_input2 = per.Entry_Placeholder_password(
            self.signup_passFrame2,
            placeholder="Repeat password",
            show_image="image/show.png",
            hide_image="image/hide.png",
        )
        self.signup_passFrame2.pack(padx=15, pady=20)

        self.SignupB = tb.Button(self.signupTab, text="Sign up", command=self.signup)
        self.SignupB.pack(padx=10, pady=15)

        self.signup_status = tb.Label(self.signupTab, text="")
        self.signup_status.pack()
        # =======================================================================================
        self.notebook.add(self.loginTab, text="login")
        self.notebook.add(self.signupTab, text="signup")
        self.notebook.select(self.loginTab)

    def start(self):
        self.resizable(0, 0)
        self.mainloop()

    def login(self):
        send_data = {
            "username": self.user_input.get().strip(),
            "password": self.pass_input.get().strip(),
        }
        respone = requests.post(url="http://127.0.0.1:5000/login", json=send_data)
        if respone.status_code != 200:
            self.login_status.config(bootstyle=DANGER, text=respone.json()["message"])
        else:
            self.login_status.config(bootstyle=SUCCESS, text=respone.json()["message"])

    def signup(self):
        send_data = {
            "username": self.signup_user_input.get().strip(),
            "email": self.signup_email_input.get().strip(),
            "password1": self.signup_pass_input1.get().strip(),
            "password2": self.signup_pass_input2.get().strip(),
        }
        respone = requests.post(url="http://127.0.0.1:5000/signup", json=send_data)
        if respone.status_code != 200:
            self.signup_status.configure(bootstyle=DANGER, text=respone.json()["message"])
        elif respone.status_code == 200:
            self.signup_status.configure(bootstyle=SUCCESS, text=respone.json()["message"])


if __name__ == "__main__":
    app = gg()
    app.start()
