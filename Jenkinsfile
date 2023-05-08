pipeline {
    agent any 
    stages {
        stage('Stage Prueba') {
            steps {
                echo 'Hello world!' 
            }
        }
        stage('Stage Prueba 2') {
            steps {
                sh 'pwd' 
            }
        }
        stage('Stage Prueba 3') {
            steps {
                sh 'env' 
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
        stage('Stage Prueba 5') {
            steps {
                sh 'pwd' 
            }
        }
        stage('Stage Prueba 6') {
            steps {
                sh 'env' 
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
