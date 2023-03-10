from seleniumbase import BaseCase

class UploadTest(BaseCase):
    def test_visible_upload(self):
        # open page
        self.open("https://the-internet.herokuapp.com/upload")

        # get file path
        file_path ='./data/pies poro.png'

        # upload file
        self.choose_file("#file-upload", file_path)

        # click the upload button
        self.click("#file-submit")

        # assert file uploaded text
        self.assert_text("File Uploaded!", '#content > div > h3')

    def test_hidden_upload(self):
        # open page
        self.open("https://practice.automationbro.com/cart/")

        # get file path
        file_path = './data/pies poro.png'

        # upload file
        self.choose_file('#upfile_1', file_path)

        # click the upload button
        self.click('#upload_1')

        # assert file uploaded text
        self.assert_text('uploaded successfully', '#wfu_messageblock_header_1_label_1')

        #Skończyłem na 1:17