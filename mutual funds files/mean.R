setwd("/home/abinash/Dropbox/peaky blenders/mutual funds files")

aditya<-read.csv("Aditya.csv")
aditya<-aditya[,c(-1,-2)]
aditya<-apply(as.matrix(aditya), 2, as.numeric)
aditya<-colMeans(aditya, na.rm = TRUE)
aditya<-aditya [!is.nan(aditya)]

hdfc<-read.csv("HDFC.csv")
hdfc<-hdfc[,c(-1,-2)]
hdfc<-apply(as.matrix(hdfc), 2, as.numeric)
hdfc<-colMeans(hdfc, na.rm = TRUE)
hdfc<-hdfc [!is.nan(hdfc)]

icici<-read.csv("ICICI.csv")
icici<-icici[,c(-1,-2)]
icici<-apply(as.matrix(icici), 2, as.numeric)
icici<-colMeans(icici, na.rm = TRUE)
icici<-icici [!is.nan(icici)]

reliance<-read.csv("Reliance.csv")
reliance<-reliance[,c(-1,-2)]
reliance<-apply(as.matrix(reliance), 2, as.numeric)
reliance<-colMeans(reliance, na.rm = TRUE)
reliance<-reliance [!is.nan(reliance)]

sbi<-read.csv("SBI.csv")
sbi<-sbi[,c(-1,-2)]
sbi<-apply(as.matrix(sbi), 2, as.numeric)
sbi<-colMeans(sbi, na.rm = TRUE)
sbi<-sbi [!is.nan(sbi)]

sundaram<-read.csv("Sundaram.csv")
sundaram<-sundaram[,c(-1,-2)]
sundaram<-apply(as.matrix(sundaram), 2, as.numeric)
sundaram<-colMeans(sundaram, na.rm = TRUE)
sundaram<-sundaram [!is.nan(sundaram)]

tata<-read.csv("Tata.csv")
tata<-tata[,c(-1,-2)]
tata<-apply(as.matrix(tata), 2, as.numeric)
tata<-colMeans(tata, na.rm = TRUE)
tata<-tata [!is.nan(tata)]

uti<-read.csv("Uti.csv")
uti<-uti[,c(-1)]
uti<-apply(as.matrix(uti), 2, as.numeric)
uti<-colMeans(uti, na.rm = TRUE)
uti<-uti [!is.nan(uti)]
