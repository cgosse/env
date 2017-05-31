# env
system configuration

# CPU scaling
install cpufreq-utils
edit /etc/init.d/cpufreq.. set to performance

##SBT
vim ~/.sbt/0.13/global.sbt
publishTo := Some(Resolver.file("file",  new File(Path.userHome.absolutePath+"/.m2/repository")))

