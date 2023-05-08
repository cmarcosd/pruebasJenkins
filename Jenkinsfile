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
                git credentialsId: '04814891-877d-4ae0-8692-fb706f2b73ae', url: 'https://github.com/cmarcosd/pruebasJenkins.git'
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
