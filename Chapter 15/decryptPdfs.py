#! python3
#decryptPdfs - decrypt pdfs with inputted passwords
import PyPDF2, os, send2trash
from pathlib import Path

userDir = input('What directory are the PDFs in?\n')
userPW = input('What is the password?\n')
os.chdir(userDir)

#Main program - goes through all PDFs
for folderName, subfolders, filenames in os.walk(userDir):
    print('The current folder is ' + folderName)
    for filename in filenames:

        #This is where the PDFs are identified
        if filename.endswith('.pdf'):
            pdfFile = open(filename, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            if not pdfReader.isEncrypted:
                print('%s is not encrypted' % filename)
                continue
            try:
                pdfReader.decrypt(userPW)
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
            except:
                print("Password '%s' does not match %s password" % (userPW,filename))
                continue

            decryptedName = (Path(folderName + '\\' + filename)).stem + '_decrypted.pdf'
            decryptedPdf = open(decryptedName,'wb')
            pdfWriter.write(decryptedPdf)
            decryptedPdf.close()
            pdfFile.close()
            send2trash.send2trash(filename)
            print('A decrypted copy of the file %s has been created and the old file has been trashed' % filename)


print('All files that could have been decrypted has been decrypted')
