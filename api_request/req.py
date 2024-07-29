import requests

data = {
    'header': '''Delivered-To: patilmanav22@gmail.com
Received: by 2002:a05:7022:380b:b0:84:eb00:fc0 with SMTP id pj11csp1552075dlb;
        Sun, 28 Jul 2024 11:02:31 -0700 (PDT)
X-Google-Smtp-Source: AGHT+IHwxvNsjXQw/KZh6nZ2nfHhzQjlt/xxs6mdeKr3qr3K8R5Hn7svguipQ5p7YP64bO6G9kl/
X-Received: by 2002:a05:6808:3013:b0:3da:ae19:ef0 with SMTP id 5614622812f47-3db23cd8a83mr6040247b6e.49.1722189751307;
        Sun, 28 Jul 2024 11:02:31 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1722189751; cv=none;
        d=google.com; s=arc-20160816;
        b=N9BZ0sf6kaQZ5lGKs/ZOhj6pfXG/l1Vn+DJJ+5/jRPYJwRR2+Sb+iBeHk31maqroQm
         SbiJ4VfkyiMQl/msaySbXSpNg68w1GbXrMWea8uCaA/x8MMct50XgzRlkRS1giq22bI2
         z6yPGzlkI8qQKhabYbEKqkYB5TjZHTXSiO5Z/KEQOlPTTOltO/5dYFX+wSmPCCkL0M34
         rR8aXXbUHO0bP1rWCMRq4MMABfheOaTA+ECJuzmB3lBKjhGS1lTxiboxGyNm9cmugTKK
         EHMHgYyNohf+ztVONqtUG0TWzbh+FCb3a9SgZ0YRVvsSN4o8zPGV5X+Re5qfY+e44b/3
         E69g==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=list-unsubscribe-post:feedback-id:reply-to:list-unsubscribe
         :content-transfer-encoding:mime-version:message-id:subject:from:to
         :date:dkim-signature:dkim-signature;
        bh=khmO+YZ+ZJYJTq3SbEnLLXplyXV4zkkaOuN8MQGCZ8M=;
        fh=QAQHmC3yHc8f0cANE7Kx5XP/IafOYEBlLYPNPsbP5Kc=;
        b=qitKL3G2UPHPHE6lQuYpBzLujFStBeCWPfPD++aWa4TtHOWk2Anc34z6q4sbjtnDFB
         6UHeQ0qTGowq7qzdwWN9N1PjxiJSD8K/UoSLa3XKzbpmjNzKXC2hMFzfNxI2DVdxZzq9
         X/rUoK/pQHz6/W8CGVNAnvuQnaslQa8KK3yl30ltwX042F/Vig0MbBdQ4yFkKrUVfWDt
         hXahnVfwTfv3zNZUTAYdVDRoUmzR0NQxBGdfL68H+MiG/5QgPPFlhciohB1y190V6LDU
         nxGjdLbofL4+sFy4/LOMDJ722kxJ3Sj2o/84H/t0zl8Yx9sO0AZGd5qIOio+QgYdeBzj
         wRjQ==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@ncb.flipkart.com header.s=nc header.b=XokK97HS;
       dkim=pass header.i=@env.etransmail.com header.s=fnc header.b=eJx6wOkF;
       spf=pass (google.com: domain of 17221050943167511-106048-1-gmail.com@delivery.ncb.flipkart.com designates 175.158.68.117 as permitted sender) smtp.mailfrom=17221050943167511-106048-1-gmail.com@delivery.ncb.flipkart.com;
       dmarc=pass (p=QUARANTINE sp=QUARANTINE dis=NONE) header.from=flipkart.com
Return-Path: <17221050943167511-106048-1-gmail.com@delivery.ncb.flipkart.com>
Received: from mta-68.117.etransmail.com (mta-68.117.etransmail.com. [175.158.68.117])
        by mx.google.com with ESMTPS id d2e1a72fcca58-70ead89b47fsi8288594b3a.268.2024.07.28.11.02.30
        for <patilmanav22@gmail.com>
        (version=TLS1_3 cipher=TLS_AES_256_GCM_SHA384 bits=256/256);
        Sun, 28 Jul 2024 11:02:31 -0700 (PDT)
Received-SPF: pass (google.com: domain of 17221050943167511-106048-1-gmail.com@delivery.ncb.flipkart.com designates 175.158.68.117 as permitted sender) client-ip=175.158.68.117;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@ncb.flipkart.com header.s=nc header.b=XokK97HS;
       dkim=pass header.i=@env.etransmail.com header.s=fnc header.b=eJx6wOkF;
       spf=pass (google.com: domain of 17221050943167511-106048-1-gmail.com@delivery.ncb.flipkart.com designates 175.158.68.117 as permitted sender) smtp.mailfrom=17221050943167511-106048-1-gmail.com@delivery.ncb.flipkart.com;
       dmarc=pass (p=QUARANTINE sp=QUARANTINE dis=NONE) header.from=flipkart.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=ncb.flipkart.com; s=nc; h=list-unsubscribe-post:feedback-id:reply-to:list-unsubscribe:
	 content-transfer-encoding:content-type:mime-version:message-id:subject:from:to:
	 from:to:subject; bh=khmO+YZ+ZJYJTq3SbEnLLXplyXV4zkkaOuN8MQGCZ8M=; b=XokK97HSsxpv4MT9y9CWx3xGpv1I8A+aHjKz05ntBdXiP/ieoO8yHXhqiDr2QFqhSyGgIo17YsbU6
	 AvNiR/OwkYnNZmQAHugvmIEQGECtZABtBchUvx6ty28ov9kxcBhwjgnUwq7hmo/H06HYAAop0SDfAq
	 9Lmb0JHRuanMkAa36zCm/57kBDdG2lnD1/1Zg0xpam7vYFFHBtkOhM2hMVABjYGd4PNZW5kC4g5WZI
	 PdAzcZ1X69SYcl0BAm22w283bk6kwqSZkFXpobGx9o4ORg8BIObztYlCa1+4kptvifT3REm2xKp/1E
	 Y9ZdsAl9M6GdZpe1vXsNYx9Jd494YxQ==
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=env.etransmail.com; s=fnc; h=list-unsubscribe-post:feedback-id:reply-to:list-unsubscribe:
	 content-transfer-encoding:content-type:mime-version:message-id:subject:from:to:
	 from:to:subject; bh=khmO+YZ+ZJYJTq3SbEnLLXplyXV4zkkaOuN8MQGCZ8M=; b=eJx6wOkFMMkvDfl3cNSocYxxY7ZtcyBeywvb4SoEon5Sda1hj/jotgq52GdOw9ibPeHCgvlcvOdE2
	 KO8b43M0VZ6yQnSoVT64cvbaGCPARTG0C6I5zKmvBpcpJp6erNMnY9BjUfb93T9tbYZIqu8CILGp6j
	 n+2uNiEzmZAImmXY=
Date: Sun, 28 Jul 2024 23:32:30 +0530
To: "Patilmanav22@gmail.com" <patilmanav22@gmail.com>
From: Flipkart <no-reply@ncb.flipkart.com>
Subject: Help us in serving you better!

Message-Id: <zjcxks17221050943167511@ncb.flipkart.com>
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="_----------=_172218975036465695"
Content-Transfer-Encoding: binary
List-Unsubscribe: <https://delivery.ncb.flipkart.com/KCEUSP?id=106048=Mx4JCVJUUwIOREFGQ0URRBhEEkUQGBkZFBhFRUIYRBlGQhkYQkJDFhYYQUZDRRFEGFROV1QKAA9WCQdXBgAHDl9TAVxTV1AADg5WBFcGVFZbVAtXBFtYWwZcVxlTD1YLV1IMCFtWUAcAD1RXUhlZEEwUQV8fF11cWFETABBBSlcFABdeDgsTXVdKFUgAClxLcyd3MGNoBlBQRBNW>, <mailto:17221050943167511-106048-fncunsub@usub.ftrans03.com?subject=Unsubscribe>
Reply-To: reply@flipkart.com
Feedback-Id: 106048:202407:1:falconide
X-Job: flipkartpromostream:106048:202407
X-Fncid: 106048-17221050943167511-0
X-Abuse-Reports-To: abuse@pepipost.com
X-Injtime: 1722189750
X-Traffic-Type: 106048-2
X-Mta-Source: flipkartpromostream_106048
X-Mailer: NetcoreCloud Mailer
List-Unsubscribe-Post: List-Unsubscribe=One-Click

--_----------=_172218975036465695
Content-Disposition: inline
Content-Transfer-Encoding: quoted-printable
Content-Type: text/plain; charset="utf-8"



 =20
  =20
  =20
  =20
  =20
  =20
  =20
 =20
=20
  =20
  =20
  =20
  =20
  =20
    =20
     =20
      =20
      =20
      =20
      =20
      =20
        =20
         =20
         =20
          =20
          =20
            =20
               Your opinion matters!  =20
            =20
          =20
           =20
         =20
        =20
      =20
      =20
      =20
      =20
        =20
         =20
          =20
          =20
            =20
                 =20
                 =20
                 =20
                 =20
            =20
            =20
             =20
              =20
              =20
                =20
                =20
              =20
               =20
            =20
          =20
           =20
         =20
        =20
      =20
       =20
     =20
    =20
  =20
  =20
  =20
  =20
    =20
     =20
      =20
      =20
        =20
         =20
         =20
          =20
           =20
           =20
             =20
                 Dear Prabhakar,    We would like to understand your paymen=
t experience for your recent purchase on Flipkart so that we can ensure a s=
eamless experience for you in the future. Please fill in the survey form he=
re . In case you are not comfortable answering any question, you may choose=
 to skip it and move to the next one.    Thanks,  Flipkart Team   =20
             =20
           =20
           =20
          =20
        =20
      =20
       =20
      =20
      =20
      =20
      =20
      =20
        =20
         =20
             =20
         =20
          =20
          =20
            =20
                       =20
            =20
          =20
          =20
          =20
          =20
            =20
               We hope you enjoy emails from Flipkart. If you wish to unsub=
scribe, please click here .  =20
            =20
          =20
           =20
         =20
        =20
      =20
      =20
       =20
    =20
  =20
  =20
    =20
 =A0


--_----------=_172218975036465695
Content-Disposition: inline
Content-Transfer-Encoding: quoted-printable
Content-Type: text/html; charset="utf-8"

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.=
w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns=3D"http://www.w3.org/1999/xhtml">
 <head>=20
  <!-- If you delete this tag, the sky will fall on your head -->=20
  <meta name=3D"viewport" content=3D"width=3Ddevice-width;initial-scale=3D1=
.0; user-scalable=3D1;">=20
  <meta http-equiv=3D"Content-Type" content=3D"text/html; charset=3DUTF-8">=
=20
  <meta http-equiv=3D"X-UA-Compatible" content=3D"IE=3Dedge">=20
  <title>Flipkart.com</title>=20
  <style type=3D"text/css">

        /*********************************/



        /* Reset CSS styles starts */



        /*********************************/



        body {

            -webkit-font-smoothing: antialiased;

            -webkit-text-size-adjust: none;

            width: 100%;

            height: 100%;

            margin: 0;

            padding: 0;

            background-color: #ffffff;

            font-family: Arial, Tahoma, Verdana, sans-serif;

            font-weight: 299px;

            font-size: 13px;

        }



        /* outlook.com / hotmail */



        .ExternalClass {

            width: 100%;

        }



        .ExternalClass,

        .ExternalClass p,

        .ExternalClass span,

        .ExternalClass font,

        .ExternalClass td,

        .ExternalClass div {

            line-height: 100%;

        }



        /* outlook 2007 / 2010 / 2013 */



        table {

            mso-table-lspace: 0pt;

            mso-table-rspace: 0pt;

        }



        img {

            -ms-interpolation-mode: bicubic;

        }



        /* OSX / iOS / windows mobile */



        body {

            -webkit-text-size-adjust: 100%;

            -ms-text-size-adjust: 100%;

        }



        img {

            border: 0px;

        }



        a:link {

            color: #666666;

            text-decoration: none;

        }



        a:visited {

            color: #666666;

            text-decoration: none;

        }



        a:hover {

            color: #2271B2;

            text-decoration: underline;

        }



        /*********************************/



        /* Email related styles */



        /*********************************/



        .body-wrapper {

            margin: 0px auto;

        }



        p,

        div {

            margin: 0;

            padding: 0;

        }



        .footer {

            border-bottom: solid 1px #e6e6e6;

        }



        * {

            margin: 0;

            padding: 0;

            font-family: "Helvetica Neue", "Helvetica", Helvetica, Arial, s=
ans-serif;

        }



        img {

            max-width: 100%;

        }



        p,

        ul {

            margin-bottom: 10px;

            font-weight: normal;

            font-size: 14px;

            line-height: 1.6;

        }



        .collapse {

            margin: 0 !important;

        }



        a {

            color: #2BA6CB;

        }



        @media only screen and (max-width: 640px) {

            a[class=3D"btn"] {

                display: block !important;

                margin-bottom: 10px !important;

                background-image: none !important;

                margin-right: 0 !important;

            }



            div[class=3D"column"] {

                width: auto !important;

                float: none !important;

            }



            table.social div[class=3D"column"] {

                width: auto !important;

            }



            img.respImg {

                width: 50%;

            }



            .h1 {

                font-size: 13px !important;

            }



            .column-wrap {

                width: 100%;

            }



            table {

                width: 100% !important;

            }



            table div {

                float: none !important;

                width: 100% !important;

            }

        }

    </style>=20
 </head>=20
 <body style=3D"-webkit-font-smoothing:antialiased; -webkit-text-size-adjus=
t:none; width: 100%; height: 100%; margin:0; padding:0; background-color:#f=
fffff; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-s=
erif;font-weight:300;" bgcolor=3D"#ffffff">
  <img style=3D"width:1px;height:1px;" src=3D"http://l.flipkart.com/t/open/=
Pqt5dGC5tS9HKrZzbsZoVGykmmMKN3-Snpf0jQ7zGSRc9XXtFp5IGP9FcSx1Mq2VOW31arA72LL=
bHlhATX2abRPUvj_XEIMdK5nms_MO7pfsJqs8JxAbwl0orsaGC9Nt7MPjJm9EvOD3XAuGgDzsnX=
_mBLhEH1DjlyzhPFZICRKXvH4GIgfk8IIXheEgZbAtRr1R9HFYT931FX57cnfUXu1kCBFEKWZq8=
YfZawhquNH57RJbsF8RRMbVGjhgnDU4JgECWdXk1KcsRYs_nRUdBjU36y2SjAsZFKxdRn0bJH3Y=
wV6Q2fiGjF58sDtZaaHMhMbtTm9pgUM0w02tCuqYP4Lg-XyWFDrZl6-Ieypxz75pthiZW0jP6Ad=
eSxabC5fP?e=3Dtrue">=20
  <!-- Wrapper table for outlook 2000 / 2002 / 2003/ 2007 / 2010 / 2013 and=
 Lotus notes 8 & 8.5 -->=20
  <!--[if (gte mso 9)|(IE)]>

<table width=3D"600" class=3D"body-wrapper" cellspacing=3D"0" align=3D"cent=
er" cellpadding=3D"0">

    <tr>

        <td valign=3D"top" align=3D"center">

<![endif]-->=20
  <table width=3D"100%" class=3D"body-wrapper" cellspacing=3D"10" align=3D"=
center" cellpadding=3D"0">=20
   <tbody>
    <tr>=20
     <td valign=3D"top" align=3D"center" width=3D"100%">=20
      <!-- =3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=
=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=
=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D -->=20
      <!-- HEADER -->=20
      <!-- =3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=
=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=
=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D -->=20
      <table class=3D"head-wrap" width=3D"100%" cellspacing=3D"0" cellpaddi=
ng=3D"0">=20
       <tbody>
        <tr>=20
         <td></td>=20
         <td class=3D"header container" style=3D"display:block; max-width:6=
00px; margin:0 auto; clear:both;">=20
          <table width=3D"100%" cellspacing=3D"0" cellpadding=3D"0">=20
           <tbody>
            <tr>=20
             <td valign=3D"middle" align=3D"left"> <font style=3D"font-size=
:12px; font-family:Arial, Helvetica, sans-serif; color:#aaaaaa"> Your opini=
on matters! </font> </td>=20
            </tr>=20
           </tbody>
          </table> </td>=20
         <td></td>=20
        </tr>=20
       </tbody>
      </table>=20
      <table class=3D"head-wrap" width=3D"100%" cellspacing=3D"0" cellpaddi=
ng=3D"0">=20
       <tbody>
        <tr>=20
         <td class=3D"header container" style=3D"display:block; max-width:6=
00px; margin:0 auto; clear:both;">=20
          <table width=3D"100%" cellspacing=3D"0" cellpadding=3D"0">=20
           <tbody>
            <tr>=20
             <td align=3D"left" valign=3D"middle" height=3D"50" width=3D"50=
%" style=3D"padding-right: 10px;"> <a lname=3D"Head:Head:Head:genImg1:R2;C1=
" href=3D"https://delivery.ncb.flipkart.com/KCEUSP?id=3D106048=3DJR4JCVJUUw=
IORFkHVgMDVFwFAlwJXQ5cBA0EBldaVgtSWl0PUlYGB1MMAF5TAABUD1FOV1QKAA9WCQdXBgAHD=
l9TAVxTV1AADg5WBFcGVFZbVAtXBFtYWwZcVxlTD1YLV1IMCFtWUAcAD1RXUhlZEEwUQV8fF11c=
WFETABBBSlcFABdeDgsTXVdKFUgAClxLcyd3MGNoBlBQRBNW&fl=3DDhZNSFhNTFoYXg0PEw5QF=
kxKUQpdF00WV1QMBgkXFk8IFUxnPSoAYFRBNSsoXAQtWj0LEQZLSFVGXyIoKQtWSQg7f0oxDQBM=
UwgjNVUqe1FXAWdWXVVUSBl8BDQvQjtTKy98dwA9WwJwSyVTKyFuIE4qRi5USG9hYl0mJgUJNlg=
cKEp9NxcXTwJ+MSkrA3wlYBxjUmFuchQZCjINK1csdBcaC2c9UgBzWGkDFwUjVi0NKmUyUg9VSQ=
BvNlQ6TjNgAlNTaSUIF3RveTIFKgFFDWctBgJifwF+QgguVFdOCAxVUw1ZGhEqZQJMEzwHH0YMc=
hJWAGFfbml7Xh0cAV0efS5PDGEKPTl9BFYrHA4PAi5nHgpVQmJmcEJKKVcyewJ8UlQMW1MIDGFj=
VS4INwB1HU9XSjRGD15SR2o8IjFuE1FeJXx0LRsBeF1rOQgmPAVSS1FLMmNqfXd+AD0GD3EsdDE=
qAA0HVRIbYlQiLVsheQlbMnwKUltoX0YMDFQuSi92Fg9aV1E3VQN8TiIJLRxCUw4sbSJITXt7XG=
8hFDJAUHQXBHxKIQkBb2QPKwIlN3xJDwpnVll+CFJQUzAoT0oxS0sYC0IhCgVnZVQxFC4LRTJcK=
FFQBXMBSX9PNSYPTwJtKRJpeywFO3RQUjMrFjVQHA4cbRVbem8BTQwrDVZAKxQiLntuAC0oYkJC=
AwxWHAguDS4GHXh+c1JAeggvFXsdSylPal4FEA4GQmIsMyIAAyFSBgMoRQ1AX3pLNi8sAVN4MTJ=
XWihQVV9/bVUWUx1iFUk2BxZRcGZmbklVUSBr&ext=3DZT10cnVl" style=3D"text-decorat=
ion:none;display:table;"> <img src=3D"https://img1a.flixcart.com/www/email/=
images/20150609-173157-logopsd__1_.png" style=3D"border:none;color:#818181;=
font-size:9px;display:table-cell; margin-right: 5px;"> </a> </td>=20
             <td align=3D"right" style=3D"border-right:1px solid #cccccc;te=
xt-align: center;padding-right: 5px;"> <a lname=3D"Head:Head:Head:genImg1:R=
2;C1" href=3D"https://delivery.ncb.flipkart.com/KCEUSP?id=3D106048=3DJR4JCV=
JUUwIORFZeBlAHVwxXClMFWQALBgFcUVpZVgkHVA8PUlRRDgBeUQMCVwRcXgdOV1QKAA9WCQdXB=
gAHDl9TAVxTV1AADg5WBFcGVFZbVAtXBFtYWwZcVxlTD1YLV1IMCFtWUAcAD1RXUhlZEEwUQV8f=
F11cWFETABBBSlcFABdeDgsTXVdKFUgAClxLcyd3MGNoBlBQRBNW&fl=3DDhZNSFhNTFoYXg0PE=
w5QFkxKUQpdF00WV1QMBgkXFk8IFUxnPSoAYFRBNSsoXAQtWj0LEQZLSFVGXyIoKQtWSQg7f0ox=
DQBMUghMNhMyey9XMXoqW3F2WAVoJxdaASJLFCxUXQgXLQMObBgcDCsBLFIFflBnXENdTGgzHFd=
2B0MnOmlNJQxRAQBKIwNbUFIzfi5qM3Z7TE1HV1ZIL34cXg81D31VNzdQd0pVKyRWRR5XXGcvHW=
h+Tl9uBhwVez1UViNVeQ4zBFt3agAIKBdHKkkDdDoDewtAVU4NHzN3IH4iN1JRPVQxBkdSOwsZN=
xwQXApVV1FfD2MHSyMuDw0JawEUFEAhEBpeYXUsEDITXjZZJmIrYE5dY0xWEDYXYQl9Ak9/SwoU=
JlBZDlM2FR9eIU0+Zy0EXmF/V3AMViRNImkuFHZeDggLb3B/NFUlB18zdzEHFGhfDHplTwgHGHk=
8YQk3dkIWByV+ZlYkEBImfhV2D2oVX3BVSW1PAQM9Wyx1HxhRDgUFUXVvVS9LN1ZUEH4sBTxzWl=
tKGVYiUxdbVG8pEEN/NyVSAHRiVCIUHFIWf0lBNWBfdH4HWUg9Kl0pVygkD1s1ODJAc0opLSkvX=
BJuCH8uXVN7QV5cKjUTVw9oERNmSicuMFR4SDcFAjdDKnkLSghqfQpYcVEfKwVTE1AUIVZeU1Aa=
WmdMLh4WUX0lWxxTEn9SamFMaFEOKFwLalcJDGkyLTl7eAA1EikJHClqUWo1BAp6Q2sLLjQqdQx=
tMxJ4USdWOXAOCwotVBFUJWghVRVbSn9sZ2o9BFUMIXUVI2t0JgwxYmBWFVYMCmE0bgtIJA0F&e=
xt=3DZT10cnVl" style=3D"text-decoration:none;"> <img src=3D"https://rukmini=
m1.flixcart.com/www/256/256/promos/18/06/2021/b6fd9929-a0f0-4e80-876a-a1493=
a97f5fc.png?q=3D100" style=3D"max-height: 64px;border:none;color:#818181;fo=
nt-size:9px;"> </a> </td>=20
             <td align=3D"right" style=3D"border-right:1px solid #cccccc; t=
ext-align: center;"> <a lname=3D"Head:Head:Head:genImg1:R2;C1" href=3D"http=
s://delivery.ncb.flipkart.com/KCEUSP?id=3D106048=3DJR4JCVJUUwIORAIDAgFQUwFR=
C1ZVAVxbVg5dVwZZBwlWAVtaVVBRBQEBAF9VAAZXAAJOV1QKAA9WCQdXBgAHDl9TAVxTV1AADg5=
WBFcGVFZbVAtXBFtYWwZcVxlTD1YLV1IMCFtWUAcAD1RXUhlZEEwUQV8fF11cWFETABBBSlcFAB=
deDgsTXVdKFUgAClxLcyd3MGNoBlBQRBNW&fl=3DDhZNSFhNTFoYXg0PEw5QFkxKUQpdF00WV1Q=
MBgkXFk8IFUxnPSoAYFRBNSsoXAQtWj0LAlxpCnRseSZQJHMJUSNQbFssDCF+AHsAEhcQUBdoCE=
ENBVB/TQ1tBCcbTw4IPAYBdhRQAUBZchdTBCp2CEgoS1xpf3VpfW5WITpnCngjMntvJyZOU3R+M=
CwAA1UsUyxoCmpsDAlmDBURLXA3UjRVV38sUQRdXnIVIjEAVjd5V3YpfHZsQUNWKiAJAFJzPChU=
VBIhAWxydxQwFzd5ElYjRxdHel1tUkA8Vjh1M28/LH1qMw8HXG9SUQlQKnMXfwx/IwBzXVFSWTc=
/M1cSdCkLUkkbMFRyYXU2KhVcWj1vL2MrXgxgbQR2Ng8OWlRuMAVsdQ4EDG9vShA0OwZnPlNXZR=
NqYW92f1ldVjhvAQosCm0PTyk2AFkOBxY1N180XRRoJFROUH1MTStdGnAzSF8adW8aJztiR34TE=
SFXYz1gIgAtVXZgUlZnE1VPCz5sIhtzUlNPFUNuTQYVJS5HKXY0XBAICVZ6TA5IXQRRDm4BO31C=
AzMrRmJ+LC4zMhwBaSZoXQdPDAsGfgMLT1kxXw8YUE07DTJlbHQyFSkPUjtrBwEGWWpSenBnJzE=
VQQ5PCTF4cVYDLwV4SlccBhVoHX4gSFN4DUFpXXATEStVKnotJVB8VAQhTA9zUzNWAVI2ChJXAH=
ZXSlZRVSoEAAADQDMFDWIQMS1UeAtMEycoWy10AmMkCUxXfkdzXFEvWyphFAttdygQMVB7XlgIE=
TFmCg80eCoGYm1wWGcpOhZoFGoUNWNZGhMrcllfVj5RKmcCXVwKNA0F&ext=3DZT10cnVl" sty=
le=3D"text-decoration:none;"> <img src=3D"https://rukminim1.flixcart.com/ww=
w/256/256/promos/18/06/2021/42138fd7-e0ff-48b5-8246-f4bebfe023f3.png?q=3D10=
0" style=3D"max-height: 64px;border:none;color:#818181;font-size:9px;"> </a=
> </td>=20
             <td align=3D"right" style=3D"text-align: center;"> <a lname=3D=
"Head:Head:Head:genImg1:R2;C1" href=3D"https://delivery.ncb.flipkart.com/KC=
EUSP?id=3D106048=3DJR4JCVJUUwIORAJXB1VTAQFXBFEDDQ9bAAoGBwBcUQsCWw9cAVtSDwMI=
VFJbVVJTXVNOV1QKAA9WCQdXBgAHDl9TAVxTV1AADg5WBFcGVFZbVAtXBFtYWwZcVxlTD1YLV1I=
MCFtWUAcAD1RXUhlZEEwUQV8fF11cWFETABBBSlcFABdeDgsTXVdKFUgAClxLcyd3MGNoBlBQRB=
NW&fl=3DDhZNSFhNTFoYXg0PEw5QFkxKUQpdF00WV1QMBgkXNgguMX5WBDg7ZlN+GAU8B0gFSyp=
0BFkASEEZSyEDA1wDUCcsVw8yNltpenkKLQodSzV0FHYuaHZMVVpKDQobfFZzVAR4XFYPOU9Tfj=
gkDlEBBlNWSiB0SW1/RQhcUlJZMXgKGlNJACUMUXNCBiJWHX1JYStjB0hBCWt9VCQwIXkXYQohT=
1oVOwRSA0hUCwEiaQMAJ2YPUVFaa0R/Ny8lTxVxMCgLaQoTNFtXShYyJRNAU1YrfFRVC1d8X1on=
AThQHW1SOkh6UxNRY1VJOzY6HUBQf0lrKm9zSHECWys1U3lXaDMSUUIxK1J8YGFVHjoSbjxLJWQ=
mcQ0ASH1eDAoPSVNcPilOdS4NB3dhTQtWAAYGNg0DBCdDFVBqQG5XATBLEUAvUkEVWwxRAFtUJg=
0QUwcLVTB/NQhoUXJfABcELgwqT1EXXWoSU1UCA3IWDQswYV1xD2Yqdn1baXxCBwY0XBYAXiBVY=
hAsJwVQTBEyPFJLAAxTYzx8e39df0goAAVXU2kqKWNiNVMMe0V7TDUaJ3wCCA9zVWF8TGEDbRYy=
IVtcazQAa3JaDS94QWskV1cCX1Z0B19VAQlvW0FpCBMLe1AUESlxfBEhVm9FVRIrMwx/KUEhBhF=
jW2oOTVw1JztsDVIRW0tsAzcPWG5cCCIhCXhVfwhZP1dQUQkBVgcHNA0CCygAZk41NxpgemcEKD=
o9XjdnKFkgR0tUUAdsCyE1AT1eEAdtbQk7M14bSjUuVVdFU1MxBipGDQ5xa2FSBiNZVlgUIG9+B=
gEZdwBrFgo3VEJcUx1WJA0F&ext=3DZT10cnVl" style=3D"text-decoration:none;"> <i=
mg src=3D"https://rukminim1.flixcart.com/www/256/256/promos/18/06/2021/e9ee=
2635-6ef6-47bd-adad-6927e4a6b3a5.png?q=3D100" style=3D"max-height: 64px;bor=
der:none;color:#818181;font-size:9px;"> </a> </td>=20
            </tr>=20
            <tr>=20
             <td valign=3D"middle" height=3D"50" align=3D"center">=20
              <table width=3D"100%" style=3D"max-width:500px;">=20
               <tbody>
                <tr>=20
                </tr>=20
               </tbody>
              </table> </td>=20
            </tr>=20
           </tbody>
          </table> </td>=20
         <td></td>=20
        </tr>=20
       </tbody>
      </table> </td>=20
     <td></td>=20
    </tr>=20
   </tbody>
  </table>=20
  <table width=3D"100%" border=3D"0" cellspacing=3D"0" cellpadding=3D"0" bg=
color=3D"#FFFFFF">=20
   <tbody>
    <tr>=20
     <td style=3D"display:block;margin:0 auto; clear:both;max-width:600px;"=
>=20
      <table bgcolor=3D"#f5f5f5" style=3D"width:100%;border-collapse:collap=
se;margin-bottom:10px">=20
       <tbody>
        <tr>=20
         <td></td>=20
         <td bgcolor=3D"#FFFFFF" style=3D"display:block;max-width:600px;mar=
gin:0 auto;clear:both">=20
          <div style=3D"border-bottom:0px solid rgb(215,215,215);border-rig=
ht:0px solid rgb(215,215,215);padding:15px 15px 0 15px;max-width:600px;marg=
in:0 auto;display:block">=20
           <table style=3D"width:100%">=20
            <tbody>
             <tr>=20
              <td style=3D"padding-top:20px;padding-bottom:40px"> <p> <font=
 style=3D"font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-weig=
ht:300;line-height:20px;text-align:left;font-size:14px;color:#333;padding:1=
3px 0 0 0"> Dear Prabhakar, </font> <br><br> <font style=3D"font-family:'He=
lvetica Neue',Helvetica,Arial,sans-serif;font-weight:300;line-height:20px;t=
ext-align:left;font-size:14px;color:#333;padding:0px 0 0 0"> We would like =
to understand your <b>payment experience</b> for your recent purchase on Fl=
ipkart so that we can ensure a seamless experience for you in the future.<b=
r><br> Please fill in the survey form <a href=3D"https://delivery.ncb.flipk=
art.com/KCEUSP?id=3D106048=3DJR4JCVJUUwIORFYAAAMIBV5QVgcAD19fVw8HUlYLAVheUl=
xdUVYHDgMBUlMHVQYBWlJOV1QKAA9WCQdXBgAHDl9TAVxTV1AADg5WBFcGVFZbVAtXBFtYWwZcV=
xlTD1YLV1IMCFtWUAcAD1RXUhlZEEwUQV8fF11cWFETABBBSlcFABdeDgsTXVdKFUgAClxLcyd3=
MGNoBlBQRBNW&fl=3DDhZNSFhNTFoYXg0PEw5QFkxKUQpdF00WV1QMBgkXNgguMX5WBDg7ZlN+G=
AU8B0gFSyp0AFhsQ15kVl1XDggIV1YMDA1TOlN/WwgnJ1cvUisVB2UuRF5aek16BjNVfChMDBBu=
WjMDWn1MVBJXElxSPn0dQDZxC14LZXUSCiB2UFpUW3J1KSYgY3NKCAkFCnM1XQMCIgV1dk0CACk=
gLGsVYCQlQ1JTEBcDWWgrAwBTAQxrJUMsAVFyFHVfAyMvdj4MKAFfSSwBCgRiDC4NVRN0PFELfi=
Z/UA1SdnkmLyFMEm4sW2ZrBlshWnILGVEbNFYUXzReNngBS3RibSZIB1MdfTQUDGsaViJBQGwoC=
jMqewcILW0uSm5+aH1sKilXcQsPXzgIbSQzEUJ7XTIEEyBYUA4LUD98b3F3eEIxCDBTLE0RD1hW=
Myw8Zw91AEsEMkkUfw9HAURpfXdeQQAJCVIvbxIRSHMbIFJBTHwJNzEpAClpUXsGBFELbH5IUDx=
WDDVzKFZLDzQoIWEbTlUPNhJ4EWAcUDNfXlVYel0oEjR7AE88GA0OJzYEUU55Aw85Ol4FQVd0Kl=
gLb3tsVx0PBlICUFEIags9Ui9nXlRYFCw3VSJxA1UVWHJYfVZnBFFQTTEAN1dzfRgsK194Si8CM=
h1JHVw0fzJ4YmYLQ3sCFQYJBg4MI1J3NysZRwZ7GVYPPAc+TCxqMGBeaHx+ASMtERUAVw0wSXsW=
VldwXkE7VDETRAYAB1YWAn9xanBRFyIPYSxwUS0MdTcBVAIBbwoyGy1XVwsGXAcFCUlBdVwpFyd=
5EUsgEH0LVVdRZwJ7CgsGLEFVDTtaIl0KfnNYWjYoPVcmCFMuf0gRLg8ODgU=3D&ext=3DZT10c=
nVl">here</a>.<br><br> In case you are not comfortable answering any questi=
on, you may choose to skip it and move to the next one.<br> </font> <font s=
tyle=3D"font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-weight=
:300;line-height:20px;text-align:left;font-size:14px;color:#333;padding:13p=
x 0 0 0"> <br> Thanks, <br> Flipkart Team </font> </p> </td>=20
             </tr>=20
            </tbody>
           </table>=20
          </div></td>=20
        </tr>=20
       </tbody>
      </table> <output></output>=20
      <!-- =3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=
=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=
=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D -->=20
      <!-- Footer Text -->=20
      <!-- =3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=
=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=
=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D -->=20
      <table class=3D"footer-wrap" width=3D"100%" cellspacing=3D"0" cellpad=
ding=3D"0">=20
       <tbody>
        <tr>=20
         <td></td>=20
         <td style=3D"display:block;margin:0 auto; clear:both;max-width:600=
px;"> <a style=3D"border:0; text-decoration:none;" href=3D"https://delivery=
.ncb.flipkart.com/KCEUSP?id=3D106048=3DJR4JCVJUUwIORFEFBQcEVg1VBgMGXFtdBQBQ=
A1JdAQkAUAxbUgRQVA4PVwcHVFRRDABOV1QKAA9WCQdXBgAHDl9TAVxTV1AADg5WBFcGVFZbVAt=
XBFtYWwZcVxlTD1YLV1IMCFtWUAcAD1RXUhlZEEwUQV8fF11cWFETABBBSlcFABdeDgsTXVdKFU=
gAClxLcyd3MGNoBlBQRBNW&fl=3DDhZNSFhNTFoYXg0PEw5QFkxKUQpdF00WV1QMBgkXFk8IFUx=
nPSoAYFRBNSsoXAQtWj0LCwlAAVBQXQ4uIF1VbAcUYAggMCJVAHEjIiJWeBxcIGAcWlcIQHwVM1=
ENbhxhORJmARcOAGVxCywLVyxFIHkAZQZEd21yAH1cFiV8E29LEXBSMVcIBm92LDEKPEJcSzJKE=
F1aS3sFbBNSO2AmCAsnYGAHBRpjcHAlIQ03aANJVwsXcktmQGx7LiMOfiELBVF+YTMgAkV4ThYf=
LBF1IH0yXh11C357QkkpSDFfVlMOTwFxNi8RAlVhNDUbMnINXjdAIWV2fl4DYC0EAUoxDBw9QHI=
FFwYBYl03URYmBwBwCgUjU0lPAXFIIAAMCAhDNRRYVzhaKll8Zy9TDBcINFU+WgBJSnNrQHIgEh=
R5VnMSGGZaCSsHaUZbBj4NPEIQVR1iSEoKak5/axIDGHwGaDRQZm4jKSIBVVkmS1sTXApqNFZVc=
Xlmf1NUUTdRcAh7DAdvfxIoAkQBSzIOEiJ+HH0RBlJRXGt6WUkxMiNnA1sWDmFACBsPcntVORc5=
JAQlXTBWImhLY08ZSDQ8PV0lQxMtCkFaCFViVBUIISsVbgwBUVRVWVJBCgVtFCYgXixpKihzayt=
bUlIGWjMnBiJ3LXQmcwJbDVBRWHMrUSR8MV0BMXRLMCsQXVN8IBMaMWtTczJFFHhpYGoEdCgoCE=
4NUAUIdw0OIAZdXFAIVRUXXjNzUGJSRnFeXkAKBycXbVQPOQtJagBaFEBacBIFNCRWDnEwUxZHb=
01ofFEBMyN0&ext=3DZT10cnVl"> <img src=3D"https://rukminim1.flixcart.com/www=
/600/240/promos/30/04/2021/f4c07fc6-b7b4-4be4-8af6-0755a292f4cf.jpg?q=3D100=
"> </a> </td>=20
         <td class=3D"container" style=3D"border-top:3px solid #333333; dis=
play:block; max-width:600px; margin:0 auto; clear:both;">=20
          <table width=3D"100%" cellspacing=3D"0" cellpadding=3D"0" align=
=3D"center" style=3D"font-family:Arial,serif;font-size:12px;font-weight:300=
;margin-top: 5px;">=20
           <tbody>
            <tr>=20
             <td align=3D"center" valign=3D"top" width=3D"100%"> <a lname=
=3D"Foot:Foot:Foot:genImg3:R1;C1" style=3D"border:0; text-decoration:none;"=
 href=3D"https://delivery.ncb.flipkart.com/KCEUSP?id=3D106048=3DJR4JCVJUUwI=
ORFZWV1NUAABSV11SXQELB1pWV1BcXAkDUFwLAANTA1JdVV4BVwVVW1dOV1QKAA9WCQdXBgAHDl=
9TAVxTV1AADg5WBFcGVFZbVAtXBFtYWwZcVxlTD1YLV1IMCFtWUAcAD1RXUhlZEEwUQV8fF11cW=
FETABBBSlcFABdeDgsTXVdKFUgAClxLcyd3MGNoBlBQRBNW&fl=3DDhZNSFhNTFoYXg0PEw5QFk=
xKUQpdF00WV1QMBgkXFk8IFUxnPSoAYFRBNSsoXAQtWj0LAmhNcXR2ew4OJ0gpDx5TD1wnIy50f=
WpUDAkOUFFcDnELfXYMeAZUKQ0WQRAUFBV/VjE7OWdxQggoKzx4ClE2VQdpVWFffHcWHzEVV2gr=
Vgt6GjsqWntPJj46KBwdVAdfKFp/cl9lYgdRFFIoUFAsDUpQOC9RAX01VVEVBTdcDFk0fwtTWAA=
MBjYqaFFuIggKXw4IOWZRXjUQFRFhLnMLAhQHCwhKAV0wHy5WI3VTAEpzPT0XG2F6Lg0nOkgnXi=
NESFIPW359QB0AWmcLex49SG4AEAdzYn1SIgsCeABwIAE9ZVZzaXZBOjIBXAZ9BDQIVygaUlxva=
gkSFhF7NEgOQjBWVQh0YWsNClJSFgwtEQ50JBZXW1JCLDcZK2UBd1N6K3ZVQ3ZjCD00BU0QYFRb=
d0EHIzBiUwkbXjwpZyILDHMSSXx2AUYKEzcxfAZzAj1/VgE3JGVzXC4sMxFaXQ4DAzF0bn9bcls=
2MVtMSUpfOFxpBg4ydW9dJgRQNUkRYTFWIQVIX3RtalBQL08PDwEOelNQDVVjBl4vVlU3XA99B1=
YuQHVyWA1WMyNVbyEAMRNSUSYKWlpgcggtVVxDPWsnHwBhCn99X3EqOiNVVQwTEXUOKCEGBFh6L=
CcZEnhUbCh0NH9+Ukl9UzcPV1YGbhQDSF06UQRpXG8LExEMRzBNNF0MeWlOfGd1NjQsUikMARN4=
bQ4TE2B6YRs8BjxcIwxRfAQBcXMAe1IfBixtF3cfJm0JJRUmUEEOUVASLnQAAFdTEg0F&ext=3D=
ZT10cnVl"> <img src=3D"https://img1a.flixcart.com/www/email/images/20150302=
-161344-flipkartFacebook.gif" style=3D"vertical-align:middle; border:none;c=
olor:#818181;font-size:9px;"> </a> <a lname=3D"Foot:Foot:Foot:genTxt4:R1;C2=
" style=3D"border:0; text-decoration:none;" href=3D"https://delivery.ncb.fl=
ipkart.com/KCEUSP?id=3D106048=3DJR4JCVJUUwIORFZXVgBXXA8GUF0EXAlbDA1SXAAOVw5=
WUw0BV1BTVwFZVF9TAVRVDFVOV1QKAA9WCQdXBgAHDl9TAVxTV1AADg5WBFcGVFZbVAtXBFtYWw=
ZcVxlTD1YLV1IMCFtWUAcAD1RXUhlZEEwUQV8fF11cWFETABBBSlcFABdeDgsTXVdKFUgAClxLc=
yd3MGNoBlBQRBNW&fl=3DDhZNSFhNTFoYXg0PEw5QFkxKUQpdF00WV1QMBgkXFk8IFUxnPSoAYF=
RBNSsoXAQtWj0LEQZLSFVGXyIoKQtWSQg7f0oxDQBMVQFRVzQVfA1LL2AgQnJ6V3Z9UAxaTh13U=
TNPSRsxLnBhfwcyEC5aAmEdfC5USG9hYl0mJgUJNlgcKEp9NxcXTwBMUh5bUXA+CwUAFENQVFNE=
VDABV1QSVRMUVFoUPQVYXXAmFC1WRSZ/HW0/A1dmFH4AECkTUx4MJCV4bzAEFgNjb1M0JCJ/HAE=
OSlQEDmNMQm8LMzZ9DwFeB3BSLi86dw8BESQ1HW4CSyxGCX9ndHtAfVMuI2kcZjc9TX5WARpcRH=
omKxMfexdrHEFWQFpuTHJIFVNWewtUKjJ1XAANKXtwTQMqV1VSFVkBelVRdg5yeV42XA5JCH4FV=
FENCiskW2luUSUgUmdWXAxbE3N5SFxFexM/BxUhDBwoUHYwBBpyTHspUQsdB1NBAGU9SmpqegV/=
LC9XcVNmMQdadk8hUgVuCgJeDA4BKn4uYVd0f21xeHEEDwAMLVsOUlIBFjsZQwZBJyAwLHw3VyF=
IJAFBUEkCcQtcLUgtCiMOQFwRNwlZb1MTUTAufR10AUUzXFJpdl9oOgMuDBdNXzdtVwEOEXVUbC=
0pBwNBCwsoVg8Bck1mRkAMBABiMHscN3AKJhoGf0ZrIwobFHASdAwGBklwQFoCaSE/J2AvdwEYV=
AobVzFfb2IGUwwzRC9WAHUrAQhrcXkBDD9bThxpMwZDbhMKCWEbaw5LFlRQFmEiCwJZc3BDZXdX=
FVV+F3cfJm0JJRUmUEEOUVASLnQAAFdTEg0F&ext=3DZT10cnVl"> <img src=3D"https://i=
mg1a.flixcart.com/www/email/images/20150302-161353-flipkartTwitter.gif" sty=
le=3D"vertical-align:middle;border:none;color:#818181;font-size:9px;"> </a>=
 <a lname=3D"Foot:Foot:Foot:genTxt5:R1;C2" style=3D"border:0; text-decorati=
on:none;" href=3D"https://delivery.ncb.flipkart.com/KCEUSP?id=3D106048=3DJR=
4JCVJUUwIORFZRBgEHAF1QBlECClgLDVsGVFVcAQtWVA4NBlBVVAUBVlZSUghdCFJOV1QKAA9WC=
QdXBgAHDl9TAVxTV1AADg5WBFcGVFZbVAtXBFtYWwZcVxlTD1YLV1IMCFtWUAcAD1RXUhlZEEwU=
QV8fF11cWFETABBBSlcFABdeDgsTXVdKFUgAClxLcyd3MGNoBlBQRBNW&fl=3DDhZNSFhNTFoYX=
g0PEw5QFkxKUQpdF00WV1QMBgkXFk8IFUxnPSoAYFRBNSsoXAQtWj0LFnR+DW59XQ8qUW4tTgQ4=
DmoyLQBselUkCy4xSQIBBUtSAVMLQ2IBLCskQlUAAyNYdloBJVNFCRQqDx9VBQ4pY1NUSG9hYl0=
mJgUJNlgcKEp9NxcXTwJSEy8ANlcuXg95UwdvDA8MDSQxKWIhcSNUXFJbDlp5dWcYCTQASTJWK2=
gfZWIMdG5pAABPbCdzXzd0WwVQC1BhfQU5DS9gVXojRwt1S11Te2oQDQlXCwEoPU5ZKAElU1BPG=
FNSEkANfj0BA0Jcf2tndw02LlEMcQITcU4UElppXE4WVw5VVg1WKgcdRldISFpAExIHDRZJHA10=
aTAmIW9fajA1DShoIVMxbVBIVm92VWwdUhtaNVIIUXJ+EjgtA3BtVVcQF35XAVVRJnJTflQGDS8=
wMQALVF8bCH0vCxtSBggGEjAMX1Z2UF1USUAJbUBUCy8Ofy1rCC91YjgOIUd7dxcLMlB4AHBcRz=
0Dfm5dR1RWASBpDQ8oWnVBWzoRT2deVhAuV3MAUlxmPHRrTgsNCC4UBWs7YS4WFEEpMSBhRVQHV=
SUuaCxNJkU2CG1sVlNdFRwUWxxeARZSTBQ9U0JnQgInOVRfKQAyaihCDlMNdlsvNxRAMHoeFA9R=
FgwPc0ZACF43KnUcWz0FFAcIQ1QAQRAjDnstVSI6e2hPIzVYeVsSKTYOcAgLJm0JVEJgCHdgIx0=
ScwxhLRNRUlYsFHdgaBhWIgIANmgQV1NzXEtwWn8LPD0NBVs/O1RuFisZG1FwOQ0QMlwTTTxIEg=
0F&ext=3DZT10cnVl"> <img src=3D"https://img1a.flixcart.com/www/email/images=
/20150302-161334-flipkartInstagram.gif" style=3D"vertical-align:middle;bord=
er:none;color:#818181;font-size:9px;"> </a> </td>=20
            </tr>=20
           </tbody>
          </table>=20
          <table width=3D"100%" cellspacing=3D"5" cellpadding=3D"0" align=
=3D"center" style=3D"font-family:Arial,serif;font-size:12px;font-weight:300=
;">=20
           <tbody>
            <tr>=20
             <td align=3D"center" valign=3D"top" width=3D"100%"> <font face=
=3D"Arial, sans-serif" color=3D"#333333" style=3D"font-size:9px;"> We hope =
you enjoy emails from Flipkart. If you wish to unsubscribe, please <a style=
=3D"font-size:9px;" href=3D"https://delivery.ncb.flipkart.com/KCEUSP?id=3D1=
06048=3DJR4JCVJUUwIORFYHAVNSVA1dAlZWXAEAAQtVXVoOVQsABFoBVgRXAlNbBAJVUAlQWlR=
OV1QKAA9WCQdXBgAHDl9TAVxTV1AADg5WBFcGVFZbVAtXBFtYWwZcVxlTD1YLV1IMCFtWUAcAD1=
RXUhlZEEwUQV8fF11cWFETABBBSlcFABdeDgsTXVdKFUgAClxLcyd3MGNoBlBQRBNW&fl=3DDhZ=
NSFhNTFoYXg0PEw5QFkxKUQpdF00WV1QMBgkXFk8IFUxnPSoAYFRBNSsoXAQtWj0LFFJaX2FMfj=
EhF3YCD18lD2dPFTJuXGIyBzkpbitIO2MPQg1DSwF8KQAqWiZAUScLClYEBl0FDQhWKiMAUmAPY=
FdVAXcJenkyDxtcUkwFUmFyAS8rXld1FD8IAX02dzRrCERae0NrbiQMK1BJXFQBTmsEWgpHWFw4=
KjQHAy53V3wOelVcDVIKMxc3bVBdIzJ/dTVXJwZVCwAjOgtpIlMdbVBnVA9NGVwxMzRtKAkpKXh=
MNVQsb0ZcDysiPUdJWSteKFNqaHVlVFYvBV9SADwOUEsaUSAbfUkzKAcLCR11AwMMfn9QW1xwHw=
cFbA1fFS0KXzsSAnFGTTtWVDFjKmJdfw9WAFNzQgsPUSpMPFQkVHsIG1slf1NBCSEPJ0IMQQ1bA=
GhSTn4BCUhUDFkzShU9SEE3IzZVWwkmEBNdCTRdImgIWlN8egxbLiErCBVoAlYPVDYaMWF+ewxV=
Og5GKG8ecSFkQQh6DAk1FDRzKXQyIV5NKQMkeXxBBzUsPHUUYCwCLUlUFEwDYVETCE8RSzVTdXE=
lNwAPW0IgHzNUXS5CC2ItU3sASn5dAVI0VwZLKxdXSj0SNAEBZyc3NDZdEnYOBjx2cg9WXkIXL1=
QMFlMwD3BRAQcJbFJoUw4VXGEQeg1KPVloWHxuWVcwVnI8fVEnfn0ENTpcW08RIhdSAgpZIFstU=
XleQFheFlUYYjELEzpjWQYNM2JCeTcrMFxHLgoxeSZnDlFMd3MrNVBiPWlVV1pqUhdVAXp3OAkS=
UFYNXCBUEnwNTFFtURQiMWkUbi9VTFktKFNgfG04AhU8awlxLkM9BVNbUVhhBiNPYVJjCSVcVzA=
aLnBvTBYvGzZbFGktYi5mbBR9W1U9PzVfXUMNB3MLVxUsB2RIFQ4KP2ZUUjQEJFRdakFVWiZQBG=
g=3D&ext=3DZT10cnVl">click here</a>. </font> </td>=20
            </tr>=20
           </tbody>
          </table> </td>=20
         <td></td>=20
        </tr>=20
       </tbody>
      </table>=20
      <!-- /FOOTER --> </td>=20
    </tr>=20
   </tbody>
  </table>=20
  <!--[if (gte mso 9)|(IE)]>

</td>

</tr>

</table>

<![endif]-->  =20
 <p>&nbsp;<br></p>
<img src=3D'https://delivery.ncb.flipkart.com/KCEUSP?id=3D106048=3DKR4JCVJU=
UwIOREFGQ0URRBhEEkUQGBkZFBhFRUIYRBlGQhkYQkJDFhYYQUZDRRFEGFROV1QKAA9WCQdXBgA=
HDl9TAVxTV1AADg5WBFcGVFZbVAtXBFtYWwZcVxlTD1YLV1IMCFtWUAcAD1RXUhlZEEwUQV8fF1=
1cWFETABBBSlcFABdeDgsTXVdKFUgAClxLcyd3MGNoBlBQRBNW' alt=3D'' /></body>
</html>
--_----------=_172218975036465695--''',
}
url = 'http://127.0.0.1:8080/header_analysis'
v = requests.post(url=url,json=data)
print("Output start heree\n" ,v.json(), "\nOutput Ends heree\n")