pipeline {
    agent any 
    stages {
        stage('Stage Prueba') {
            steps {
                sh 'echo Hello world!' 
            }
        }
        stage('Stage PIP') {
            steps {
                sh 'pip list' 
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
        stage('Run tests') {
            steps {
                // Paso para ejecutar las pruebas de pytest
                sh 'pytest .\test_calculator.py'
            }
        }
    }
}
