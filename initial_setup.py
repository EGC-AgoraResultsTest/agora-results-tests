import os

def main(){
	# Iniciar el entorno virtual
	os.system('workon prueba')

	# Realizar la instalación de agora results traido de git
	os.system('pip install git+https://github.com/agoravoting/agora-results.git')

}

if __name__ == "__main__":
    main()



