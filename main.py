from time import sleep
from format import main
from warnings_email import geraWarning

i=0
if __name__ == "__main__":
    while True:
        try:
            main()
            if i!=0:
                geraWarning('Conexão restabelecida')
                i=0
        except:
            i=i+1
            if i==1:
                i=i+1
                geraWarning('Headers com erro, renove.')
        sleep(60)
       
