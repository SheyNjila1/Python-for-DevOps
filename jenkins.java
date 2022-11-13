node{
 def mavenHome = tool name: 'maven3.8.6' 
    stage('SCM Clone') {
        git credentialsId: 'github-credentials', url: 'https://github.com/SheyNjila1/spring-boot-docker.git'
    
    }    
  
    stage('MavenBuild'){
      sh '${mavenHome}/bin/mvn clean package'
    }

    stage('SonarQuebeReport') {
      //sh '${mavenHome}/bin/mvn sonar:sonar'
    }

    stage('UploadNexus') {
      //sh docker build -t mylandmarktech/spring-boot-mongo

    }

    stage('BuildDockerImage') {
      sh 'docker build -t mylandmarktech/spring-boot-mongo .'
}

}

#####
node{
    stage('SCM Clone') {
        git credentialsId: 'github-credentials', url: 'https://github.com/SheyNjila1/spring-boot-docker.git'
    }    
 

}