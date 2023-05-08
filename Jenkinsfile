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
                git credentialsId: '9279d6b3-5bb8-49c0-9eb2-8397cfb5dea9', url: 'https://github.com/cmarcosd/pruebasJenkins.git'
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
