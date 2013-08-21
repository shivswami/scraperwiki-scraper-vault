import scraperwiki
import lxml.html
import bs4
import urllib2

# Blank Python

#url="http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=MP&ITIDistrict=CDW"
links=['http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=BAU', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=BAU', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=BAU', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=BAU', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=BAU', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=BAU', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=BAU', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=BAU', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=BAU', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=BAU', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=BDR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=BDR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=BDR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=BDR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=BDR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=BDR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=BDR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=BDR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=BDR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=BDR', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=BEG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=BEG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=BEG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=BEG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=BEG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=BEG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=BEG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=BEG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=BEG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=BEG', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=BEL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=BEL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=BEL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=BEL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=BEL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=BEL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=BEL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=BEL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=BEL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=BEL', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=BGK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=BGK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=BGK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=BGK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=BGK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=BGK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=BGK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=BGK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=BGK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=BGK', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=BGR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=BGR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=BGR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=BGR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=BGR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=BGR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=BGR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=BGR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=BGR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=BGR', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=BIJ', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=BIJ', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=BIJ', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=BIJ', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=BIJ', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=BIJ', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=BIJ', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=BIJ', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=BIJ', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=BIJ', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=CHI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=CHI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=CHI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=CHI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=CHI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=CHI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=CHI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=CHI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=CHI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=CHI', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=CIK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=CIK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=CIK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=CIK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=CIK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=CIK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=CIK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=CIK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=CIK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=CIK', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=CKM', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=CKM', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=CKM', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=CKM', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=CKM', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=CKM', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=CKM', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=CKM', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=CKM', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=CKM', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=CMN', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=CMN', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=CMN', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=CMN', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=CMN', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=CMN', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=CMN', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=CMN', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=CMN', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=CMN', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=DHA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=DHA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=DHA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=DHA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=DHA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=DHA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=DHA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=DHA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=DHA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=DHA', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=DKK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=DKK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=DKK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=DKK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=DKK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=DKK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=DKK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=DKK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=DKK', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=DKK', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=DVA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=DVA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=DVA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=DVA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=DVA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=DVA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=DVA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=DVA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=DVA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=DVA', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=GDG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=GDG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=GDG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=GDG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=GDG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=GDG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=GDG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=GDG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=GDG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=GDG', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=GUL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=GUL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=GUL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=GUL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=GUL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=GUL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=GUL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=GUL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=GUL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=GUL', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=HAS', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=HAS', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=HAS', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=HAS', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=HAS', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=HAS', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=HAS', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=HAS', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=HAS', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=HAS', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=HAV', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=HAV', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=HAV', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=HAV', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=HAV', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=HAV', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=HAV', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=HAV', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=HAV', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=HAV', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=HBI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=HBI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=HBI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=HBI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=HBI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=HBI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=HBI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=HBI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=HBI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=HBI', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=KOD', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=KOD', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=KOD', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=KOD', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=KOD', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=KOD', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=KOD', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=KOD', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=KOD', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=KOD', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=KOL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=KOL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=KOL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=KOL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=KOL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=KOL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=KOL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=KOL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=KOL', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=KOL', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=KPP', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=KPP', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=KPP', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=KPP', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=KPP', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=KPP', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=KPP', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=KPP', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=KPP', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=KPP', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=KRW', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=KRW', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=KRW', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=KRW', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=KRW', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=KRW', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=KRW', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=KRW', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=KRW', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=KRW', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=MGE', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=MGE', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=MGE', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=MGE', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=MGE', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=MGE', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=MGE', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=MGE', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=MGE', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=MGE', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=MNY', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=MNY', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=MNY', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=MNY', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=MNY', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=MNY', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=MNY', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=MNY', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=MNY', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=MNY', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=MYS', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=MYS', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=MYS', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=MYS', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=MYS', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=MYS', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=MYS', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=MYS', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=MYS', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=MYS', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=RA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=RA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=RA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=RA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=RA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=RA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=RA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=RA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=RA', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=RA', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=RCR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=RCR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=RCR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=RCR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=RCR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=RCR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=RCR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=RCR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=RCR', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=RCR', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=SHI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=SHI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=SHI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=SHI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=SHI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=SHI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=SHI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=SHI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=SHI', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=SHI', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=TUM', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=TUM', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=TUM', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=TUM', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=TUM', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=TUM', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=TUM', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=TUM', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=TUM', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=TUM', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=UDU', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=UDU', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=UDU', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=UDU', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=UDU', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=UDU', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=UDU', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=UDU', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=UDU', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=UDU', 'http://dget.nic.in/lisdapp/ITI/List/lsttcITIProfile.asp?ListType=20&ITIState=KN&ITIDistrict=YAG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=YAG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITINVerifiedDistTradeUnits.asp?ITIState=KN&ITIDistrict=YAG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ITIState=KN&ITIDistrict=YAG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=21&ITIState=KN&ITIDistrict=YAG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=22&ITIState=KN&ITIDistrict=YAG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=23&ITIState=KN&ITIDistrict=YAG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=24&ITIState=KN&ITIDistrict=YAG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=25&ITIState=KN&ITIDistrict=YAG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIGovtDistTradeUnits.asp?ListType=26&ITIState=KN&ITIDistrict=YAG', 'http://dget.nic.in/lisdapp/ITI/Reports/rpttcITIDistTradeUnits.asp?ListType=33&ITIState=KN']
sl_no=0
print len(links)
for url in links:
    print url
    try:
        l_no=url[url.find('ListType=')+9:url.find('&')]
    except:
        l_no=0
    try:
        html=urllib2.urlopen(url).read()
    except:
        continue
    start=False
    soup=bs4.BeautifulSoup(html)
    start=False
    for el in soup.find_all("table"):
        for el2 in el.find_all("tr"):
            for el3 in el2.find_all("td"):
                text= el3.get_text()
                if start:
                    sl_no+=1
                    #print (text)
                    scraperwiki.sqlite.save(unique_keys=["sl_no"],data={"sl_no":sl_no,"Data":text,"List":l_no})
                if text.find('1.')>0:
                    start=True