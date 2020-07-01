#! python3
#encryptPdfs - encrypts all unencrypted Pdfs
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

            #Checks for already encrypted PDFS
            if pdfReader.isEncrypted:
                print('%s is already encrypted' % filename)
                continue

            #Writes content of current file to writer object
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))

            #encrypted PDF is created and renamed
            pdfWriter.encrypt(userPW)
            encryptedName = (Path(folderName + '\\' + filename)).stem + '_encrypted.pdf'
            encryptedPdf = open(encryptedName,'wb')
            pdfWriter.write(encryptedPdf)
            encryptedPdf.close()
            pdfFile.close()

            #Tests if PDFs are encrypted correctly
            try:
                encryptTester = PyPDF2.PdfFileReader(open(encryptedName, 'rb'))
                encryptTester.decrypt(userPW)
                pageTest = encryptTester.getPage(0)

                #Trashes old unencrypted file
                send2trash.send2trash(filename)
                print('An encrypted copy of the file %s has been created and the old file has been trashed' % filename)

            except:
                print('An issue with encrypting %s has been found' % filename)



print('All files that could have been encrypted has been encrypted')


