from numpy import log
from tkinter import *
from tkinter import ttk


root = Tk()

class backend():

    def limpar1(self):

        #Limpeza no frame1
        self.mass11entry.delete(0, END)
        self.massprop11entry.delete(0, END)
        self.veleject11entry.delete(0, END)
        self.rest1.destroy()
        self.rocket1.destroy()

        


    def calcular1(self):
            
        #Calculos do foguete de 1 estágio
        prop11 = float((self.massprop11entry).get())
        mas11 = float((self.mass11entry).get())
        velej11 = float((self.veleject11entry).get())
        ln = log(1 + ( prop11/ mas11))
        vel1 = velej11 * ln
            
        self.final1 = StringVar()
        (self.final1).set(str(round(vel1, 2)) + " m/s") 

        #Label que mostra o resultado
        self.rocket1 = Label(self.frame1, text="Seu foguete possui uma velocidade de: ", fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.rocket1.place(relx=0.2, rely=0.9)

        self.rest1 = Label(self.frame1, textvariable=self.final1, fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.rest1.place(relx=0.45, rely=0.95)



    def limpar2(self):
        self.mass21entry.delete(0, END)
        self.massprop21entry.delete(0, END)
        self.veleject21entry.delete(0, END)
        self.mass22entry.delete(0, END)
        self.massprop22entry.delete(0, END)
        self.veleject22entry.delete(0, END)
        self.rest2.destroy()
        self.rocket2.destroy()
    
    def calcular2(self):

        #Calculos do foguete de 2 estágios

        mass21 = float((self.mass21entry).get())
        prop21 = float((self.massprop21entry).get())
        ve21 = float((self.veleject21entry).get())

        mass22 = float((self.mass22entry).get())
        prop22 = float((self.massprop22entry).get())
        ve22 = float((self.veleject22entry).get())


        masstot2 = mass21 + mass22
        ln21 = log(masstot2 / (masstot2 - prop21))
        vest21 = ve21 * ln21

        ln22 = log(mass22 / (mass22 - prop22))
        vest22 = vest21 + ve22 *ln22

        self.final2 = StringVar()
        (self.final2).set(str(round(vest22, 2)) + " m/s") 

        #Label que mostra o resultado
        self.rocket2 = Label(self.frame2, text="Seu foguete possui uma velocidade de: ", fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.rocket2.place(relx=0.2, rely=0.9)

        self.rest2 = Label(self.frame2, textvariable=self.final2, fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.rest2.place(relx=0.45, rely=0.95)

    def limpar3(self):
        self.mass31entry.delete(0, END)
        self.massprop31entry.delete(0, END)
        self.veleject31entry.delete(0, END)

        self.mass32entry.delete(0, END)
        self.massprop32entry.delete(0, END)
        self.veleject32entry.delete(0, END)

        self.mass33entry.delete(0, END)
        self.massprop33entry.delete(0, END)
        self.veleject33entry.delete(0, END)

        self.rest3.destroy()
        self.rocket3.destroy()

    def calcular3(self):

        
        #Calculos do foguete de 3 estágios

        mass31 = float((self.mass31entry).get())
        prop31 = float((self.massprop31entry).get())
        ve31 = float((self.veleject31entry).get())

        mass32 = float((self.mass32entry).get())
        prop32 = float((self.massprop32entry).get())
        ve32 = float((self.veleject32entry).get())

        mass33 = float((self.mass33entry).get())
        prop33 = float((self.massprop33entry).get())
        ve33 = float((self.veleject33entry).get())


        masstot33 = mass31 + mass32 + mass33
        masstot32 = mass32 + mass33
        ln31 = log(masstot33 / (masstot33 - prop31))
        vest31 = ve31 * ln31

        ln32 = log(masstot32 / (masstot32 - prop32))
        vest32 = vest31 + ve32 * ln32

        ln33 = log(mass33 / (masstot33 - prop33))
        vest33 = vest31 + vest32 + ve33 * ln33



        self.final3 = StringVar()
        (self.final3).set(str(round(vest33, 2)) + " m/s") 

        #Label que mostra o resultado
        self.rocket3 = Label(self.frame3, text="Seu foguete possui uma velocidade de: ", fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.rocket3.place(relx=0.2, rely=0.9)

        self.rest3 = Label(self.frame3, textvariable=self.final3, fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.rest3.place(relx=0.45, rely=0.95)





class app(backend):

    def __init__(self):
        self.root = root
        self.tela()
        self.frame0()
        self.windgetsF0()


        root.mainloop()



    def tela(self):

        self.root.title("Éder Company")
        #self.root.iconbitmap("favicon.ico")
        self.root.configure(background='white')
        self.root.geometry("696x539")
        self.root.resizable(True, True)
        self.root.minsize( width=696, height=539)
        self.root.maxsize( width=696, height=539)

        self.root.text = Label(text='Rocket Speed Calculator', bg='white', fg='#4682B4',
        font=('arial', 18, 'bold'))
        self.root.text.place(relx=0.3, rely=0.02)



    def frame0(self):

        self.frame0 = Frame(self.root, bd=4, bg='#4682B4',
        highlightbackground='white', highlightthickness=2)

        self.frame0.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.8)

    
            
    def frame1(self):

        #CONFIG DO FRAME EM GERAL
        self.frame1 = Frame(self.root, bd=4, bg='#4682B4',
        highlightbackground='white', highlightthickness=2)

        self.frame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.8)

        self.voltar = Button(self.frame1, text="Voltar", bd=2, bg='#000080', fg=
        'white', font=('arial', 9, 'bold'), command=self.frame1.destroy)
        self.voltar.place(relx= 0.03, rely =0.03, relwidth=0.12, relheight=0.06)

        self.att1 = Label(self.frame1, text='Digite Apenas Números', fg='white',
            bg ='#4682B4', font=('arial', 8 , 'bold'))
        self.att1.place(relx=0.35, rely=0.01)

        self.att2 = Label(self.frame1, text='. Para separar as casas decimais ', fg='white',
            bg ='#4682B4', font=('arial', 8 , 'bold'))
        self.att2.place(relx=0.25, rely=0.05)



        #MASSA TOTAL
        self.mass11 = Label(self.frame1, text="Massa Total:", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.mass11.place(relx=0.1, rely=0.15)

        self.mass11entry = Entry(self.frame1)
        self.mass11entry.place(relx=0.55, rely=0.15, relwidth=0.2)

        self.kg11 = Label(self.frame1, text='kg', fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.kg11.place(relx=0.75, rely=0.15)



        #MASSA DO PROPELENTE
        self.massprop11 = Label(self.frame1, text="Massa do Propeplente:", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.massprop11.place(relx=0.1, rely=0.25)

        self.massprop11entry = Entry(self.frame1)
        self.massprop11entry.place(relx=0.55, rely=0.25, relwidth=0.2)

        self.kg12 = Label(self.frame1, text='kg', fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.kg12.place(relx=0.75, rely=0.25)



        #VELOCIDADE DE EJEÇÃO
        self.veleject11 = Label(self.frame1, text="Velocidade de Ejeção:", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.veleject11.place(relx=0.1, rely=0.35)

        self.veleject11entry = Entry(self.frame1)
        self.veleject11entry.place(relx=0.55, rely=0.35, relwidth=0.2)

        self.ms11 = Label(self.frame1, text='m/s', fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.ms11.place(relx=0.75, rely=0.35)


        
        #BOTÃO DE CALCULAR
        self.calc1 = Button(self.frame1, text='Calcular',command=self.calcular1)
        self.calc1.place(relx=0.35, rely=0.85)

        #BOTÃO DE LIMPAR
        self.bt_limpar = Button(self.frame1, text= "Limpar", command= self.limpar1)
        self.bt_limpar.place(relx= 0.5, rely=0.85)

        

    def frame2(self):

        #CONFIG DO FRAME EM GERAL
        self.frame2 = Frame(self.root, bd=4, bg='#4682B4',
        highlightbackground='white', highlightthickness=2)

        self.frame2.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.8)

        self.voltar = Button(self.frame2, text="Voltar", bd=2, bg='#000080', fg=
        'white', font=('arial', 9, 'bold'), command=self.frame2.destroy)
        self.voltar.place(relx= 0.03, rely =0.03, relwidth=0.12, relheight=0.06)

        self.att12 = Label(self.frame2, text='Digite Apenas Números', fg='white',
            bg ='#4682B4', font=('arial', 8 , 'bold'))
        self.att12.place(relx=0.35, rely=0.01)

        self.att2 = Label(self.frame2, text='. Para separar as casas decimais ', fg='white',
            bg ='#4682B4', font=('arial', 8 , 'bold'))
        self.att2.place(relx=0.25, rely=0.05)



        #MASSA TOTAL 1º ESTÁGIO
        self.mass21 = Label(self.frame2, text="Massa Total", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.mass21.place(relx=0.11, rely=0.165)


        self.mass211 = Label(self.frame2, text="1º Est.", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.mass211.place(relx=0.05, rely=0.25)

        self.mass21entry = Entry(self.frame2)
        self.mass21entry.place(relx=0.18, rely=0.25, relwidth=0.16)

        self.kg21 = Label(self.frame2, text='kg', fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.kg21.place(relx=0.32, rely=0.25)

        #MASSA TOTAL ESTAGIO 2
        self.mass22 = Label(self.frame2, text="2º Est.", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.mass22.place(relx=0.05, rely=0.32)

        self.mass22entry = Entry(self.frame2)
        self.mass22entry.place(relx=0.18, rely=0.32, relwidth=0.16)

        self.kg22 = Label(self.frame2, text='kg', fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.kg22.place(relx=0.32, rely=0.32)


        #MASSA DO PROPELENTE 1º ESTÁGIO
        self.massprop21 = Label(self.frame2, text="Massa do Propeplente", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.massprop21.place(relx=0.5, rely=0.165)

        self.massprop211 = Label(self.frame2, text="1º Est.", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.massprop211.place(relx=0.53, rely=0.25)

        self.massprop21entry = Entry(self.frame2)
        self.massprop21entry.place(relx=0.66, rely=0.25, relwidth=0.16)

        self.kg21 = Label(self.frame2, text='kg', fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.kg21.place(relx=0.82, rely=0.25)


        #MASSA DO PROPELENTE ESTAGIO 2

        self.massprop22 = Label(self.frame2, text="2º Est.", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.massprop22.place(relx=0.53, rely=0.32)

        self.massprop22entry = Entry(self.frame2)
        self.massprop22entry.place(relx=0.66, rely=0.32, relwidth=0.16)

        self.kg22 = Label(self.frame2, text='kg', fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.kg22.place(relx=0.82, rely=0.32)


        #VELOCIDADE DE EJEÇÃO 1º ESTÁGIO
        self.veleject21 = Label(self.frame2, text="Velocidade de Ejeção", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.veleject21.place(relx=0.3, rely=0.51)

        self.veleject211 = Label(self.frame2, text="1º Est.", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.veleject211.place(relx=0.32, rely=0.58)

        self.veleject21entry = Entry(self.frame2)
        self.veleject21entry.place(relx=0.45, rely=0.58, relwidth=0.16)

        self.ms21 = Label(self.frame2, text='m/s', fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.ms21.place(relx=0.6, rely=0.58)


        #VELOCIDADE DE EJEÇÃO ESTAGIO 2
        self.veleject22 = Label(self.frame2, text="2º Est.", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.veleject22.place(relx=0.32, rely=0.64)

        self.veleject22entry = Entry(self.frame2)
        self.veleject22entry.place(relx=0.45, rely=0.64, relwidth=0.16)

        self.ms22 = Label(self.frame2, text='m/s', fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.ms22.place(relx=0.6, rely=0.64)


            
        #BOTÃO DE CALCULAR
        self.calc2 = Button(self.frame2, text='Calcular',command=self.calcular2)
        self.calc2.place(relx=0.35, rely=0.85)

        #BOTÃO DE LIMPAR
        self.bt_limpar2 = Button(self.frame2, text= "Limpar", command=self.limpar2)
        self.bt_limpar2.place(relx= 0.5, rely=0.85)



    def frame3(self):

        self.frame3 = Frame(self.root, bd=4, bg='#4682B4',
        highlightbackground='white', highlightthickness=2)

        self.frame3.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.8)

        self.voltar = Button(self.frame3, text="Voltar", bd=2, bg='#000080', fg=
        'white', font=('arial', 9, 'bold'), command=self.frame3.destroy)
        self.voltar.place(relx= 0.03, rely =0.03, relwidth=0.12, relheight=0.06)

        self.att3 = Label(self.frame3, text='Digite Apenas Números', fg='white',
            bg ='#4682B4', font=('arial', 8 , 'bold'))
        self.att3.place(relx=0.35, rely=0.01)

        self.att33 = Label(self.frame3, text='. Para separar as casas decimais ', fg='white',
            bg ='#4682B4', font=('arial', 8 , 'bold'))
        self.att33.place(relx=0.25, rely=0.05)



        #MASSA TOTAL 1º ESTÁGIO
        self.mass31 = Label(self.frame3, text="Massa Total", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.mass31.place(relx=0.11, rely=0.165)


        self.mass311 = Label(self.frame3, text="1º Est.", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.mass311.place(relx=0.05, rely=0.25)

        self.mass31entry = Entry(self.frame3)
        self.mass31entry.place(relx=0.18, rely=0.25, relwidth=0.16)

        self.kg31 = Label(self.frame3, text='kg', fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.kg31.place(relx=0.32, rely=0.25)

        #MASSA TOTAL ESTAGIO 2
        self.mass32 = Label(self.frame3, text="2º Est.", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.mass32.place(relx=0.05, rely=0.32)

        self.mass32entry = Entry(self.frame3)
        self.mass32entry.place(relx=0.18, rely=0.32, relwidth=0.16)

        self.kg32 = Label(self.frame3, text='kg', fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.kg32.place(relx=0.32, rely=0.32)

        #MASSA TOTAL ESTAGIO 3
        self.mass33 = Label(self.frame3, text="3º Est.", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.mass33.place(relx=0.05, rely=0.39)

        self.mass33entry = Entry(self.frame3)
        self.mass33entry.place(relx=0.18, rely=0.39, relwidth=0.16)

        self.kg33 = Label(self.frame3, text='kg', fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.kg33.place(relx=0.32, rely=0.39)


        #MASSA DO PROPELENTE 1º ESTÁGIO
        self.massprop31 = Label(self.frame3, text="Massa do Propeplente", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.massprop31.place(relx=0.5, rely=0.165)

        self.massprop311 = Label(self.frame3, text="1º Est.", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.massprop311.place(relx=0.53, rely=0.25)

        self.massprop31entry = Entry(self.frame3)
        self.massprop31entry.place(relx=0.66, rely=0.25, relwidth=0.16)

        self.kg21 = Label(self.frame3, text='kg', fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.kg21.place(relx=0.82, rely=0.25)


        #MASSA DO PROPELENTE ESTAGIO 2

        self.massprop32 = Label(self.frame3, text="2º Est.", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.massprop32.place(relx=0.53, rely=0.32)

        self.massprop32entry = Entry(self.frame3)
        self.massprop32entry.place(relx=0.66, rely=0.32, relwidth=0.16)

        self.kg32 = Label(self.frame3, text='kg', fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.kg32.place(relx=0.82, rely=0.32)

        #MASSA DO PROPELENTE ESTAGIO 3

        self.massprop33 = Label(self.frame3, text="3º Est.", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.massprop33.place(relx=0.53, rely=0.39)

        self.massprop33entry = Entry(self.frame3)
        self.massprop33entry.place(relx=0.66, rely=0.39, relwidth=0.16)

        self.kg33 = Label(self.frame3, text='kg', fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.kg33.place(relx=0.82, rely=0.39)


        #VELOCIDADE DE EJEÇÃO 1º ESTÁGIO
        self.veleject31 = Label(self.frame3, text="Velocidade de Ejeção", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.veleject31.place(relx=0.3, rely=0.51)

        self.veleject311 = Label(self.frame3, text="1º Est.", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.veleject311.place(relx=0.32, rely=0.58)

        self.veleject31entry = Entry(self.frame3)
        self.veleject31entry.place(relx=0.45, rely=0.58, relwidth=0.16)

        self.ms31 = Label(self.frame3, text='m/s', fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.ms31.place(relx=0.6, rely=0.58)


        #VELOCIDADE DE EJEÇÃO ESTAGIO 2
        self.veleject32 = Label(self.frame3, text="2º Est.", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.veleject32.place(relx=0.32, rely=0.65)

        self.veleject32entry = Entry(self.frame3)
        self.veleject32entry.place(relx=0.45, rely=0.65, relwidth=0.16)

        self.ms32 = Label(self.frame3, text='m/s', fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.ms32.place(relx=0.6, rely=0.65)


        #VELOCIDADE DE EJEÇÃO ESTAGIO 3
        self.veleject33 = Label(self.frame3, text="3º Est.", fg='white',
        bg ='#4682B4', font=('arial', 11 , 'bold'))
        self.veleject33.place(relx=0.32, rely=0.72)

        self.veleject33entry = Entry(self.frame3)
        self.veleject33entry.place(relx=0.45, rely=0.72, relwidth=0.16)

        self.ms33 = Label(self.frame3, text='m/s', fg='white',
        bg ='#4682B4', font=('arial', 10 , 'bold'))
        self.ms33.place(relx=0.6, rely=0.72)


            
        #BOTÃO DE CALCULAR
        self.calc3 = Button(self.frame3, text='Calcular',command=self.calcular3)
        self.calc3.place(relx=0.35, rely=0.85)

        #BOTÃO DE LIMPAR
        self.bt_limpar3 = Button(self.frame3, text= "Limpar", command= self.limpar3)
        self.bt_limpar3.place(relx= 0.5, rely=0.85)


    
    def windgetsF0(self):

        #FRASES
        self.bemvindo= Label(self.frame0, text='Bem-vindo(a)!',
        bg ='#4682B4', fg='white', font=('arial', 12 , 'bold'))
        self.bemvindo.place(relx=0.35, rely=0.05)

        self.estag = Label(self.frame0, text='Quantos estagios tem seu foguete ?', fg='white',
        bg ='#4682B4', font=('arial', 12 , 'bold'))
        self.estag.place(relx=0.18, rely=0.2)

        #BOTOES
        #1
        self.btone = Button(self.frame0, text="1", bd=2, bg='#000080', fg=
        'white', font=('arial', 12, 'bold'), command=self.frame1)
        self.btone.place(relx= 0.12, rely =0.4, relwidth=0.15, relheight=0.1)

        #2
        self.bttwo = Button(self.frame0, text="2", bd=2, bg='#000080', fg=
        'white', font=('arial', 12, 'bold'), command=self.frame2)
        self.bttwo.place(relx= 0.42, rely =0.4, relwidth=0.15, relheight=0.1)

        #3
        self.btthree = Button(self.frame0, text="3", bd=2, bg='#000080', fg=
        'white', font=('arial', 12, 'bold'), command=self.frame3)
        self.btthree.place(relx= 0.72, rely =0.4, relwidth=0.15, relheight=0.1)

        

app()