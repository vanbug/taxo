d=as.data.frame(cbind(c(1:10),c(11:20)))
print(d)
library('Cairo')
CairoPNG('ab.png')
?Cairo
plot(d)
dev.off()
