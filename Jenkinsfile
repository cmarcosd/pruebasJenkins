pipeline {
    agent any 
    stages {
        stage('Stage Prueba') {
            steps {
                echo 'Hello world!' 
            }
        }
        stage('Checkout') {
            steps {
                // Paso para obtener el código fuente desde el repositorio Git
                git 'https://github.com/cmarcosd/pruebasJenkins.git'
            }
        }
        stage('Run tests') {
            steps {
                // Paso para ejecutar las pruebas de pytest
                sh 'pytest'
            }
        }
    }
}
