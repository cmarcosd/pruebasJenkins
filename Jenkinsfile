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
                cleanWs()
                checkout scm: [$class: 'GitSCM', branches: [[name: '*/main']],userRemoteConfigs:
                [[url: 'https://github.com/cmarcosd/pruebasJenkins.git']]]
            }
        }
        stage('Install dependencies') {
            steps {
                // Instalar dependencias si es necesario
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                // Paso para ejecutar las pruebas de pytest
                sh 'pytest .\test_calculator.py'
            }
        }
    }
}
