node() {
  stage('checkout') {
    deleteDir()
    checkout scm
  }
  stage('build') {
    sh "behave -i test.feature --junit"
  }
  stage('publish') {
    junit 'reports/*.xml'
  }
}