import requests#10-9


url1="https://api.m.jd.com/client.action?functionId=newBabelAwardCollection&body=%7B%22activityId%22%3A%222maPuB2FfzqTEmzuebGqrZsjfhLw%22%2C%22scene%22%3A%221%22%2C%22args%22:%22key=587BD39E9A26430A39386ABE90BB169F7378905E60D43DA10EEAA793181834CCBDC7B4E6CF488AABEDFCE29D9DF314B0_bingo,roleId=66D04BB382F5BD90152EA858862C68D73826EFC9861C924C66A0F46250B2CB7CF8DC496185135B5697EC06B900F3A7D87A4D243AD9944A723B7B2447530BF027F63C8DB4EE9421EF4EFD53615B0617CFD0F98D624E4EA7DEE72883EC47B68CAE2F590E184CFDCE268CCE14E2F23A91BE1AC4887D0DDBC310E64DFFBBCB32F24A8587E958C451402FEF7746761489485A11650C7F964C0CE74C6652FA5C461A59_bingo,strengthenKey=19F512DCD8EE34ABE9C4FB4A92C2F42A8A9D01811E681B73D7CEC26742F958C2_bingo%22%2C%22log%22%3A%221652750751716~1dyh9DtTo4Ud41d8cd98f00b204e9800998ecf8427e~3%2C1~CC7A34A46AD591D3DFEB635BD9CF9235788D0D22~0nz5czt~C~ThJHVRAPa24UEEFeXhoIbm0fGlVHXhECBAwIBRQQRkMRAhAEBgYKBQAABA0DAgEDDAIHAREUEEJVVxoIF0RHTEZBVkZeEBkSRF1TFwoRXlRBUUZZR1QSHxpCUV4RAmkEAR8LHgYcBhQDGQVuFBBfWhECARkSUEsQDxICDgFTUwIBUAMHUgsLAAFRDAVTUQYNCwYJBVwABwNXCBAZEl1IEA8Sf1FcQEgTWVNHU1sOBhccEUwQDxICDgcHBwYIBQABBAkEFxwRUlkXChFZEBkSVUhQFwoRGh4XXkUaCBd3XFdVWVUTcVxWHhEUEFtRRRoIF1MRFBBGU0EaCG4IBQ8eAQADZR4XQlwaCG4SUhoeF1ERFBBUEh8aUxccEVkQGRJSGh4XURFlHhdZXFkQDxJVXlRTVlVMRhccEVlYFwoRTRAZElBREA8SRAscAB4BGh4XU1VnRBcKEQgCFxwRWlYXChFKU1tUXFUPB1RQXmF2f3IaHhddWRoIbgAfCB4FbR8aUFlfVBoIF1ERFBBYQ1QaCBdREUU%3D~1tabbuk%22%2C%22random%22%3A%222dcfSCOA%22%7D&client=wh5";

url2="https://api.m.jd.com/client.action?functionId=newBabelAwardCollection&body=%7B%22activityId%22%3A%222maPuB2FfzqTEmzuebGqrZsjfhLw%22%2C%22scene%22%3A%221%22%2C%22args%22:%22key=587BD39E9A26430A39386ABE90BB169F7378905E60D43DA10EEAA793181834CCBDC7B4E6CF488AABEDFCE29D9DF314B0_bingo,roleId=66D04BB382F5BD90152EA858862C68D73826EFC9861C924C66A0F46250B2CB7CF8DC496185135B5697EC06B900F3A7D87A4D243AD9944A723B7B2447530BF027F63C8DB4EE9421EF4EFD53615B0617CFD0F98D624E4EA7DEE72883EC47B68CAE2F590E184CFDCE268CCE14E2F23A91BE1AC4887D0DDBC310E64DFFBBCB32F24A8587E958C451402FEF7746761489485A11650C7F964C0CE74C6652FA5C461A59_bingo,strengthenKey=19F512DCD8EE34ABE9C4FB4A92C2F42A8A9D01811E681B73D7CEC26742F958C2_bingo%22%2C%22log%22%3A%221655371831594~1Ya9ifuJFc1d41d8cd98f00b204e9800998ecf8427e~1%2C1~354F8905E9D67551491106EC0A84D3CF94B921B6~1povwdf~C~TRdDWhACbWgbFUZWWxcNbG8UFFJFWRACBAECAR4aRUYVDRAJAAACBAUJDgYGAgoAAA0EAxAUFEJSUxACFEFDQ0ZMUEBRFR4aQVBWFQgaUFNDVkdZQ1QVGxBIUlsVDWkJBxkEGwEUAxkGGwdlGhddXRACBRkVVEEaDBcGAQFeVQQOVQQPVwYOAgNaAgJRVgcNDwYOAVYKBAZTBxAUFFtHFQgaelxZQkoYV1RFVFoOAhcbFUYaDBcGAQcNBQIGDwEJAwwDFR4aXF4VDRBZFBkVUUJaFA8VFR4aWEMVDRB%2FWVpQW1cYf1tUGRAUFFtWQRACFFYVGxBLVUcVDWkAAAIbAwIIaxkVRV0aDG4VVhAUFFQVGxBZFBkVVhAUFFQVGxBZFBkVVhBlGhdeWFMaDBdRUVReUFNDQxAUFFRdFQgaQxcbFVFRFA8VQAEWAxsFFR4aVVNoQRACFAUHFR4aVFEVDRBKV1tTWF8FcFh0R1VUYVkVGxBVXBcNbAIUBhkHah4aVFlYUBACFFQVGxBVRVIVDRBZFEg%3D~06byggb%22%2C%22random%22%3A%22FmCpglWl%22%7D&client=wh5";

url3="https://api.m.jd.com/client.action?functionId=newBabelAwardCollection&body=%7B%22activityId%22%3A%222maPuB2FfzqTEmzuebGqrZsjfhLw%22%2C%22scene%22%3A%221%22%2C%22args%22:%22key=587BD39E9A26430A39386ABE90BB169F7378905E60D43DA10EEAA793181834CCBDC7B4E6CF488AABEDFCE29D9DF314B0_bingo,roleId=66D04BB382F5BD90152EA858862C68D73826EFC9861C924C66A0F46250B2CB7CF8DC496185135B5697EC06B900F3A7D87A4D243AD9944A723B7B2447530BF027F63C8DB4EE9421EF4EFD53615B0617CFD0F98D624E4EA7DEE72883EC47B68CAE2F590E184CFDCE268CCE14E2F23A91BE1AC4887D0DDBC310E64DFFBBCB32F24A8587E958C451402FEF7746761489485A11650C7F964C0CE74C6652FA5C461A59_bingo,strengthenKey=19F512DCD8EE34ABE9C4FB4A92C2F42A8A9D01811E681B73D7CEC26742F958C2_bingo%22%2C%22log%22%3A%221652749539174~1XpXtGAeNgCd41d8cd98f00b204e9800998ecf8427e~3%2C1~5ED542826772A40CDFBABE26D2CDEA1663AA2491~0w3ijy4~C~ThVDXBEPbGodEUFZWhMJbmobE1RHWRULCgYOGxNARhUNEwIDAgUGBwwCBAgCAwYOBAIMFRsTRFBTFQsRQUNDRUdTQlETHxdAUlARDxVRV0dUQlZEUhcbFUFXWxUNagIEGwQdABkCGwAfAGobE1lfFQ0CHxdURBMJFwYBAlVWBg5TBQJWBAgGBFUDBlVUAgIIAAwBUwMBBlMHEx8XWUcTCRd7Xl9GTRdWUEFWXwEFERkVQxMJFwYBBAECAw4EAAwGAAURGRVdWhEPFVYTHxdRR1MRDxUVHRFbQRULEXJYWFZfUBd%2BX1AbFRsTXVRBFQsRVhUbE0BWRRULaA0BAB0HBQdqHRFHWBULaBdWFR0RVBUbE1IXGxVQERkVVhMfF1YVHRFUFWodEVxYVhMJF1FRV1VTUUNFERkVVlsRDxVCEx8XVF4TCRdABB8GGwUVHRFWUWhHEQ8VBwERGRVVVREPFUVQXVFYWgxiUnh2X1R5XBUdEVhdFQtoBRsHHQNoGxVTX1pQFQsRVBUbE15GUBULEVQVSg%3D%3D~0d9go9o%22%2C%22random%22%3A%22QgOAngLk%22%7D&client=wh5";




headers4={
           "Host": "api.m.jd.com",


    "content-type": "application/x-www-form-urlencoded",
    "accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; POT-AL00a Build/HUAWEIPOT-AL00a; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3234 MMWEBSDK/201201 Mobile Safari/537.36 MMWEBID/8008 MicroMessenger/8.0.1840(0x28000036) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",

    "origin": "https://prodev.j.com",
    "x-requested-with": "com.tencent.mm",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "referer":"https://pro.jingxi.com",
"accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",

        "Accept-Encoding": "gzip,deflate",
"x-rp-client": "h5_1.0.0",

"x-referer-page": "https://pro.jingxi.com",

"cookie":"visitkey=00256770786771686832624426;wxapp_openid=oA1P50GqbaLVVBUxQBuY4LBXm1JU;appCode=msd95910c4;shshshfpx=475014cc-b32c-9fa0-2e9c-774c85eb2714-1686834769;jdpin=jd_p7IiBJozobHPJ1d;open_id=oTGnpnJIxB7ogfy6sLJ-FvueeiRo;pin=jd_p7IiBJozobHPJ1d;wx_nickname=jd_user;b_webp=1;b_avif=1;b_dw=400;b_dh=744;b_dpr=2.700000047683716;wq_uin=200001099677901662;wq_skey=zaACB2E1EEE9C074C89AC337645DD409CF07E603E224E0BBD6F4130BDFABC864FF89C0F809FC59EB552F94DECFC2416108FAEB5C72DDC47067207F187A3412C001A7D78F1DBAD81F85AE358067DE4D51778BDCDD1C9DE6F6B966BDE03FD1EE8E39;wq_auth_token=FE7DB500AA54B7169911CFE927B5AC28F129AB4093D0461DAA16DA06EB6DD88214EF46A3CFB13C1FCC8B3D4BA79FFD77;TrackerID=c9XlUNqCK4Ssx6kp_jCQKEu5DwDA6-vJ56yiBtHamvXwZLMPXO6LtupJa4nd7372MQMjnbiYUZSp8gycmwXvkr82HRmoUd5LVFr0pib9bom8sNlgQYF1Wv3Py1qUJQ_OzJP5cecveyqaURzTmodJFA;pt_key=AAJlLZuIAEAXwoc67L6gm5l957UqSZVU-oqdkjx6qex63Dy28kwAviBquKeBtFpJra4pj0fP3eYvH3NEgKCnpcHbBQkNukXP;pt_pin=jd_p7IiBJozobHPJ1d;sfstoken=tk01mac861c0ba8sMXgzRk13TTM1fer4l3nMLofp1S8MJtzxUjI3D+OzQy7MUM7VJwkBYZlJ67yVOwtQTBtyfDs8J/NB;retina=1;webp=1;__jdc=122270672;mba_muid=754b85111268b9d97ef7e200b2716750;share_cpin=;share_open_id=;share_gpin=;shareChannel=;source_module=;erp=;sc_width=400;shshshfpa=475014cc-b32c-9fa0-2e9c-774c85eb2714-1686834769;3AB9D23F7A4B3C9B=QXFQWFDLKFC4BI6CKR7G26XQ75FMEF7ME2WWUZBLQIGGLHZKG3PVRVQO22UUX44ARWC2X4U2LSAZTTWVA7Y43YI2CE;cd_eid=jdd01w4AIF5E6MHOVDHJA3APHHEND5HPEBLMI3YGSR5MNL3PCWWNTT3ZZWPFS2NH2WCPM42HKKGRBXINJTCF7RZUWRU35QQ6SER5OQGC453GUXDFRH5UW62VHXWH6Y4D5FZ6ARXB;wxapp_version=8.22.180;buildtime=20231018;cid=5;wxapp_type=1;degrade_level=0;wxapp_uuid=1686832624197291135580;__wga=1697726839967.1697726699282.1697629869615.1695525221581.30.19;PPRD_P=EA.17078.79.1-CT.138567.7.93-LOGID.1697726840038.622615517-UUID.7616269606b56bda2a81c92e8e0b00be;e_wq_addr=CJOmCtY4Dtq5CNUvD0CnC18nCNGyXzOmDNrpDJG1CzUvD0CvdJVNDzOvdJHPCUDpTXU3COHQTXU1C0YmTXU1HJKyXyV1ENHPGyV1ENDMCIV1DJCzGV8vdJUzDJcvdJczEOSvdJq4DJcvdJumDJCvD0CvdJVNDzOvdJHPCUCvdJcmHOYvdJUzHtKvdJVPCNSvdJq0HUCvdJqzGtOvdJUzC0OvdJUzDJcvdJczEOSvdJq4DJcvdJumDJCvdJUzDOOvdJVNEUSvdJq0HOGvdJVPGUGvCtqvdJUzDJcvdJczEOSvdJY3DJOvdJUzDOOvdJVNEUSvdJUnDzKvdJHPGUGvCtuvdJUzDJcvdJczEOSvdJY3DJOnENCvdJUzHtcvD0CnCtKkENK3EJcyTJTNCzckDzq5DNS1;wq_addr=11026868905%7C13_1042_1048_54535%7C%u5C71%u4E1C_%u70DF%u53F0%u5E02_%u84EC%u83B1%u533A_%u5357%u738B%u8857%u9053%7C%u5C71%u4E1C%u70DF%u53F0%u5E02%u84EC%u83B1%u533A%u5357%u738B%u8857%u9053%u534A%u5C9B%u84DD%u5EAD%28%u5357%u738B%u6751%u534A%u5C9B%u5170%u4EAD%29%u5357%u738B%u6751183%u53F7%7C120.807972%2C37.789425;__jdv=122270672%7Cdirect%7C-%7Cnone%7C-%7C1697763667585;__jda=122270672.754b85111268b9d97ef7e200b2716750.1697315442.1697763667.1697806529.6;__jdb=122270672.1.754b85111268b9d97ef7e200b2716750|6.1697806529;mba_sid=16978065300006849298388922274.1;joyytokem=babel_2vsLWSF6ktmQqVxTrwGMt4iN3tz3MDF5S3ZOcTk5MQ==.SH1PeUlJfUN8SU59RzA0DwEPJx5Kfx4DD0hnQGJAVXoIfA9INTcPAC57GxsANQ4aDyQDBzs9H08KAyA5HQYeKwIXDTQvNh57Ej4iHgo3DzMzOiwISA4FRiIBKCAGOBQUch8dNzsAOxkgBzU=.2be29473;3AB9D23F7A4B3CSS=jdd03QXFQWFDLKFC4BI6CKR7G26XQ75FMEF7ME2WWUZBLQIGGLHZKG3PVRVQO22UUX44ARWC2X4U2LSAZTTWVA7Y43YI2CEAAAAMLJUT3JBAAAAAACJA6YSY3VJXEJUX;shshshfpb=AAmq6J02LElAUzLMsn6AunHdMhesnFBaGg0dpSgAAABJqZF9wN0lpQkpvem9iSFBKMWQ;__jd_ref_cls=Babel_LeavepageExpo;joyya=1697806527.1697806533.54.0v6339s;"

           

}
headers2={
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "Cache-Control": 'no-cache',
            "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5 Plus Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2899 MMWEBSDK/201001 Mobile Safari/537.36 MMWEBID/1486 MicroMessenger/7.0.20.1781(0x27001439) Process/toolsmp WeChat/arm64 NetType/4G Language/zh_CN ABI/arm64",
"origin": "https://pro.jingxi.com",
            "accept": "*/*",
            "connection": "Keep-Alive",
            "Accept-Encoding": "gzip,deflate"


            }

           
headers3={
           
"User-Agent": "Mozilla/5.0 (Linux; Android 7.0; SLA-AL00 Build/HUAWEISLA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2898 MMWEBSDK/191102 Mobile Safari/537.36 MMWEBID/4984 MicroMessenger/7.0.9.1560(0x27000933) Process/tools NetType/WIFI Language/zh_CN ABI/arm32",
 "Host": "api.m.jd.com",
    "content-type": "application/x-www-form-urlencoded",
    "accept": "application/json, text/plain, */*",

    "origin": "https://pro.jingxi.com",
    "x-requested-with": "com.tencent.mm",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "referer":"https://pro.jingxi.com",
"accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",

        "Accept-Encoding": "gzip,deflate",
"x-rp-client": "h5_1.0.0",

"x-referer-page": "https://pro.jingxi.com",
"cookie":"b_webp=1;b_avif=0;shshshfpa=56443212-17d3-87c6-33b6-12712801fea9-1686831977;shshshfpx=56443212-17d3-87c6-33b6-12712801fea9-1686831977;share_cpin=;share_open_id=;share_gpin=;channel=;source_module=;erp=;retina=1;appCode=msd95910c4;webp=1;shareChannel=;buy_uin=6318741733;jdpin=jd_HcVilmGHPXiq;mcossmd=eab74d73079040de9b5b5ed2d1e92677;open_id=oTGnpnHoEUBbB7mlAw-yWcdBlokQ;pin=jd_HcVilmGHPXiq;pinId=sSK7fPguPoQQa2jo2BZrmw;wq_unionid=oCwKwuBH0w7AOfaXuOe2LzRwSEYc;wx_nickname=jd_user;visitkey=66958198491601686831238351;wxapp_openid=oA1P50AoTfxs1hAz7xRwSiXD0EPM;wq_addr=10678464405|13_1042_1048_54535|%E5%B1%B1%E4%B8%9C_%E7%83%9F%E5%8F%B0%E5%B8%82_%E8%93%AC%E8%8E%B1%E5%8C%BA_%E5%8D%97%E7%8E%8B%E8%A1%97%E9%81%93|%E5%B1%B1%E4%B8%9C%E7%83%9F%E5%8F%B0%E5%B8%82%E8%93%AC%E8%8E%B1%E5%8C%BA%E5%8D%97%E7%8E%8B%E8%A1%97%E9%81%93%E5%AF%A8%E9%87%8C%E6%9D%9116|120.791998%2C37.772414;__jdc=122270672;block_call_jdapp=11;defaultHeadId=;gHeadAddressId=;gHeadPlanId=;gSId=;gDSId=;buildtime=20230915;mba_muid=168802646502965216362;b_dw=400;b_dh=673;b_dpr=1.7999999523162842;rurl=https%3A%2F%2Fcoupon.m.jd.com%2Fcoupons%2Fshow.action%3Fkey%3Dcam8cfs7o9ae4f60be78425b2e2bc7dd%26roleId%3D121160028;equipmentId=MM6FSQAGGVN376UXYEBUE62SPM54QNOVP6UOEWQKJ3BY7XW55JWUMJFBQ34SMSR4MZZPA4OHJQCMHSWIMP22IXEKXY;fingerprint=5a7d61e7c78bb33a5df382c6547ca317;deviceVersion=7.0.19.1740%280x27001310%29;deviceOS=android;deviceOSVersion=8.1.0;deviceName=WeiXin;TrackID=slZAX8Y1_WojgRW2zrZvutgq_q8U93kBXH9YKCtny62eXNR9Hg7KJBitCiFyv1jYv-KU4RuuI03AYnJT7f5bW3oG6fcjzTGEEDUF1RN6jKWxLB1aUTJTfZZTHzqNZY_Zkay_aKVqCngC5XOFwMwt03nAoFH2M9Grck6P2egfVIA;nickname_base64=;openid2=C1B57B73D5D3A1E6615515F5D553047030D09E487065EDE69E932644BED5A0FF91F9F4D87C4E47F050708ACD568D5FE2;picture_url=;pinsign=2dc0a6f28dc1bef6f440d58396a64a1f;sex=0;wq_skey=zaAD8EBEFF01F385EAA4C203977E341D250F4B64528240143F52347E07EFE0FE4F643D757CD2F49FC1D2BF6C0BFD4F74BAA2871A19E32DF5F22EFEB834B0D2D2991AA8D82799F69A45670B7B0320165A2C;wq_uin=6318741733;cid=9;__jdv=122270672%7Cdirect%7C-%7Cnone%7C-%7C1697132650762;__wga=1697132652063.1697132652063.1696349676661.1686831241821.1.25;3AB9D23F7A4B3C9B=Z3W4XZZNJNX7YVONVYO3EJ7MCJKEQU2WR26GBSZQNBOY2TBZ5F4RIUCSDS7C5PA6F3QA2SFH3LXIHQ2324CLLA4WNE;__jda=122270672.943269572755159d8a087902a3f98895.1695156927.1697647739.1697808350.8;3AB9D23F7A4B3CSS=jdd03Z3W4XZZNJNX7YVONVYO3EJ7MCJKEQU2WR26GBSZQNBOY2TBZ5F4RIUCSDS7C5PA6F3QA2SFH3LXIHQ2324CLLA4WNEAAAAMLJVBYNMYAAAAADZIGEGXCEXRYAMX;_gia_d=1;network=wifi;TrackerID=AuVi68Y_Fe5KrpIq6GabezF0A0g4GX15Xasb7DAzzf906B1lhMQ5BHUmr5TAqcbu0VjazVbSTbECbgelleLxeFN-7RjDjFFGRa4O3hy8KKlgmRp7F7OWT1xztBmWBEU09xQuosoH_49Ibw0z4y5vdw;pt_key=AAJlMn_8ADApwprYBcE1pj0MSOgknz_11psa_bTQ1MFFEa08yd5f-yr1ohanE5oSSrUtmu-kIF8;pt_pin=jd_HcVilmGHPXiq;pt_token=4ag4gbpe;pwdt_id=jd_HcVilmGHPXiq;sfstoken=tk01ma0611c26a8sMSsyeDJ4M2NKy+7+NXt2qAi4kYJYdqF4Jcaf3Xxy7eklBW6hIelsZWVjwCwAQdfrg0tX9K63RUbZ;__jdb=122270672.2.943269572755159d8a087902a3f98895|8.1697808350;mba_sid=16978083504937164033790364426.2;__jd_ref_cls=MDownLoadFloat_TopOldExpo;joyytokem=babel_2vsLWSF6ktmQqVxTrwGMt4iN3tz3MDFtam9hSDk5MQ==.XFxWVnBdUlxYeV5ZVx8NO1IWU35YP1xTNlxGWU15QVsRUzZcFC4gJSoCPlF6IS8EMDEoAgk1IFUzFRUgJxIkIABAGz0ADwoSA1IbCisuIAksFBE=.12980afb;shshshfpb=AAu4rRE2LEkQyEhfTh8YzthJxKAH-qRaGgxl3SgAAAA9qZF9IY1ZpbG1HSFBYaXE;joyya=1697808384.1697808397.72.1druzyd;"
           
      
            }

headers1={

 "Host": "api.m.jd.com",
    "content-type": "application/x-www-form-urlencoded",
    "accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; POT-AL00a Build/HUAWEIPOT-AL00a; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3234 MMWEBSDK/201201 Mobile Safari/537.36 MMWEBID/8008 MicroMessenger/8.0.1840(0x28000036) Process/toolsmp WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm64",

    "origin": "https://pro.jingxi.com",
    "x-requested-with": "com.tencent.mm",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "referer":"https://pro.jingxi.com",
"accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",

        "Accept-Encoding": "gzip,deflate",
"x-rp-client": "h5_1.0.0",

"x-referer-page": "https://pro.jingxi.com",
           "cookie":"b_webp=1;b_avif=1;appCode=msd95910c4;jdpin=gibaoxi;open_id=oTGnpnPA5IQ1FUGWMjkM-um5Ze2E;pin=gibaoxi;wx_nickname=jd_user;commonAddress=6065843065;regionAddress=13%2C1042%2C1048%2C54535;shshshfpx=677a6cc1-ce32-5ba7-a69e-b60e347828eb-1675164635;visitkey=11081520779461678240283221;wxapp_openid=oA1P50GPWXs3CuodUL4M3vaglu-k;wq_addr=11027481485%7C13_1042_1048_54535%7C%u5C71%u4E1C_%u70DF%u53F0%u5E02_%u84EC%u83B1%u533A_%u5357%u738B%u8857%u9053%7C%u5C71%u4E1C%u70DF%u53F0%u5E02%u84EC%u83B1%u533A%u5357%u738B%u8857%u9053%u534A%u5C9B%u84DD%u5EAD%28%u5357%u738B%u6751%u534A%u5C9B%u5170%u4EAD%29%u5357%u738B%u6751%7C120.807972%2C37.789425;shshshfpa=677a6cc1-ce32-5ba7-a69e-b60e347828eb-1675164635;share_cpin=;share_open_id=;share_gpin=;channel=;source_module=;erp=;wxapp_uuid=16782402830862067149;webp=1;shareChannel=;buy_uin=5313646889;mcossmd=2776247380e2a456880c18047c86a7ed;pinId=BjKFPOI-81I;wq_unionid=oCwKwuCcHLNS0kRmrNyNZIq16s0Q;e_wq_addr=CJOmCtc0ENO0ENUvD0CnC18nCNGyXzOmDNrpDJG1CzUvD0CvdJVNDzOvdJHPCUDpTXU3COHQTXU1C0YmTXU1HJKyXyV1ENHPGyV1ENDMCIV1DJCzGV8vdJUzDJcvdJczEOSvdJq4DJcvdJumDJCvD0CvdJVNDzOvdJHPCUCvdJcmHOYvdJUzHtKvdJVPCNSvdJq0HUCvdJqzGtOvdJUzC0OvdJUzDJcvdJczEOSvdJq4DJcvdJumDJCvdJUzDOOvdJVNEUSvdJq0HOGvdJVPGUGvCtqvdJUzDJcvdJczEOSvdJY3DJOvdJUzDOOvdJVNEUSvdJUnDzKvdJHPGUGvCtuvdJUzDJcvdJczEOSvdJY3DJOvD0CnCtKkENK3EJcyTJTNCzckDzq5DNS1;b_dw=400;b_dh=745;b_dpr=2.700000047683716;shshshfpb=ldm_5s3eJuwVEQe9KPKSA3w;__jdu=8b1d80804fdcc7b21d769e0730aa46ca;qid_uid=d225db8c-8efd-466a-a510-b2ae8340a285;qid_fs=1697701266108;qid_ls=1697701266108;qid_ts=1697701266160;qid_vis=1;pt_pin=gibaoxi;pwdt_id=gibaoxi;TrackerID=XtDAwhLw8734c7Xse1jXp_BDMIzdf1Wp3uzpyfOH8wofo-hrwgc4YbrZN1tBOvpWFCHnLMzrWXzwjWJeyPcwdeMFObRm9oI-W_bPkl-osQy1gkgG3qwRandM2ZBYjwFi;pt_key=AAJlMN3QADD9ZQ2-_cV6XZcQn0gMOduewHdp-AQuM66PsAzOLMMzv1EqQQZKZzDXXGWNlnYT0FY;pt_token=ag974jfj;retina=1;__wga=1697791347465.1697791001475.1697700891380.1696071661230.70.3;PPRD_P=EA.17078.79.1-CT.137081.10.1-UUID.83982c14ea7541fbc87f6b6d546411e7-LOGID.1697791347480.1244462744;pinStatus=0;wxapp_version=8.22.180;buildtime=20231018;__jdc=122270672;__jdwxapp=16782402830862067149.JA2019_5112348.wx91d27dbf599dff74.;3AB9D23F7A4B3CSS=jdd03C63JYUTJGNWNJVI4IFVJWN35SQCLGMTZO3GOIX2DOCTGVYWM7777Z5Y4FZK4QXZR4BD6JEWTRSQT465EXLO25DLYUYAAAAMLJRAKP4IAAAAADEZT6PGVWHLEEQX;3AB9D23F7A4B3C9B=C63JYUTJGNWNJVI4IFVJWN35SQCLGMTZO3GOIX2DOCTGVYWM7777Z5Y4FZK4QXZR4BD6JEWTRSQT465EXLO25DLYUY;equipmentId=C63JYUTJGNWNJVI4IFVJWN35SQCLGMTZO3GOIX2DOCTGVYWM7777Z5Y4FZK4QXZR4BD6JEWTRSQT465EXLO25DLYUY;fingerprint=b1a137d47cb28df9c8146ca9daf53166;deviceVersion=8.0.1840%280x28000036%29;deviceOS=android;deviceOSVersion=10;deviceName=WeiXin;rurl=https%3A%2F%2Fgt.m.jd.com%2Ffootprint%2Findex%3Fsource%3Dmini%26ptag%3D7155.1.10%26cookie%3D%257B%2522wxapp_type%2522%253A1%257D%23%26wxappSeries%3D%257B%2522uuid%2522%253A%252216782402830862067149%2522%252C%2522std%2522%253A%2522JA2019_5112348%2522%252C%2522seq%2522%253A45%252C%2522vts%2522%253A44%252C%2522appid%2522%253A%2522wx91d27dbf599dff74%2522%257D;TrackID=BppMoQvL1vCYkLIDkfcFV5QUS4MOVAiDP98LgYoUJRZVGQDhK5STpImUpOi0UZ6n7RjoRg1eLc2okSIyYJ0c3UHipJWM3u2wVUQTgzK1ELJ0178BXhiDwtZPhpWqZEHSx_PrUz0Rkd8fvPx4wrf7ZTyMBxD0nMxdogUG5oM6XS0;nickname_base64=;openid2=2DD50BB572E0FEA29A977A6FF681B040838C2EC1A470009E37EE5579BAE16A6892015F7BC6570094F1B1B3E0A8F33C2C;picture_url=;pinsign=7a99a6955da168fc09196b50abfa241d;sex=0;wq_skey=za6235B14C9645BEA46619C09A75FFDFE8669EBCA7BFB4156314C56BF5EB5C9DC7EB337521588CD53C1363A3CCDAA06EFA438BF851828C733BEC7BE5DF0FEC92BA67490B9CDD05F108D21AA0E231473F90;wq_uin=5313646889;country=;sfstoken=tk01wc4d11c99a8sMngxeDIrMisztzNfqU0PN67j68eb6K8NrcM9YOB1POg2LxFbDmQ4fNURNWlHwVdWfWuW6lGtKnjV;cid=5;wxapp_type=1;__jd_ref_cls=MFootPrintFloat_ListPro;__jda=122270672.52aa19b289adf22d349d72bdc3ff4a68.1697700891.1697700891.1697889424.2;mba_muid=83982c14ea7541fbc87f6b6d546411e7;wq_auth_token=328EF55559FF79DAD216C036FAD722C32CF6D88D08AC2DFF796F66AF5B0AD64C;__jdb=122270672.3.52aa19b289adf22d349d72bdc3ff4a68|2.1697889424;__jdv=122270672%7Cweixin%7Ct_1000072662_17005_001%7Cweixin%7Cdzh_h5_Menu_Fanswelfare_101%7C1697890415515;"
           
    }
            
response4= requests.post(url=url1, headers=headers4)
print(response4.text)

response3= requests.post(url=url2, headers=headers3)
print(response3.text)

response14= requests.post(url=url3, headers=headers1)
print(response14.text)




def notice(content):
    token ="c204e4622c9f4e3e8bf06591c7f6e89d"
    title = "惊喜"
    url = f"http://www.pushplus.plus/send?token={token}&title={title}&content={content}&template=html"
    response9=requests.request("GET", url)
    print(response9.text)
notice(response3.text+response4.text+response14.text)
