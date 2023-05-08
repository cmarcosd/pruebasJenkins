pipeline {
    agent any 
    stages {
        stage('Stage Prueba') {
            steps {
                bat 'echo "Hello world!"' 
            }
        }
        stage('Stage PIP') {
            steps {
                try {
                    bat 'python --version' 
                }
                catch() {
                    bat 'C:/Users/cmarcosd/AppData/Local/Programs/Python/Python310/python --version' 
                }
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
                bat 'pytest .\test_calculator.py'
            }
        }
    }
}
