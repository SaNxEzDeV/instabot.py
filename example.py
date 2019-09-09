#!/usr/bin/env python3
# -*- coding: utf-8 -*-
<<<<<<< HEAD
import os
import time

from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol

bot = InstaBot(
    login="TopTechTool",
    password="8InstagramSantos9!!",
    like_per_day=1000,
    comments_per_day=500,
    tag_list=['technologies', 'techworld', 'tech', 'future', 'gadgets', 'smarthome', 'ingenieering', 'futurism', 'tecnologia', 'dispositivos'],
    tag_blacklist=[''],
    user_blacklist={},
    max_like_for_one_tag=50,
    follow_per_day=300,
    follow_time=1 * 60 * 60,
    unfollow_per_day=300,
    unfollow_break_min=15,
    unfollow_break_max=30,
    log_mod=0,
    proxy="",
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list_en=[["This", "What a", "Such a", "That", "Wow, This", "Wow, what a"],

                  ["foto","" "imagen", "pic", "shot", "snapshot", "caption", "message"],

                  ["is", "looks", "feels", "is really", "blows my mind, it's", "is just"
                  "makes me feel great, it's"],

                  ["great, thanks for sharing this", "super, thanks for sharing, we love it", 
                    "good, thanks for that", "very good, we really like it", "super good, glad to see things like this",
                    "wow... thanks for this", "WOW....thanks a lot for this", "cool thanks for sharing",
                    "GREAT, we really like it","magnificent, we really like it", "magical, thanks for sharing",
                    "very cool....thanks a lot for this", "stylish", "beautiful", "so beautiful",
                    "so professional, glad to see things like that", "lovely, we really like it", "incredible, awesome to see things like that", 
                    "excellent, thanks a lot for this", "amazing, we really like this kind of things"],

                  [".", "..", "...", "!", "!!", "!!!"],
                  ["=)", ":)", ":-)", "^^"]
                  ],

    comment_list_es=[["Menuda", "Increible", "Esta", "Wow", "Vaya", "Vaya pedazo"],

                  ["foto", "imagen", "pic","fotazo", "mensaje"],

                  ["es", "nos parece", "es realmente", "es increiblemente", "nos ha dejado locos, es", "me parece"],
                 
                  ["genial, muchisimas gracias por compartir", "increible, gracias por sharing", "enorme el poder ver cosas asi", 
                  "muy buena, me ha encantado", "super buena, nos ha encantado, gracias", "wow...nos ha gustado mucho, gracias",
                   "WOW, muchisimas gracias", "INCREIBLE, muchas gracias por compartir",
                   "magnifica, agradecemos gente compartiendo cosas asi", "magica, muchas gracias",
                   "super chula, muchisimas gracias por compartir",
                   "professional, lo recomiendo", "super interesante, muchas gracias",
                    "excelente, gracias", "increible, enhorabuena", "impresionante, gracias"],

                  [".", "..", "...", "!", "!!", "!!!"],
                  ["=)", ":)", ":-)", "^^"]
                  ],
    # Use unwanted_username_list to block usernames containing a string
    # Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    # 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
        'second', 'stuff', 'art', 'project', 'love', 'life', 'food', 'blog',
        'free', 'keren', 'photo', 'graphy', 'indo', 'travel', 'art', 'shop',
        'store', 'sex', 'toko', 'jual', 'online', 'murah', 'jam', 'kaos',
        'case', 'baju', 'fashion', 'corp', 'tas', 'butik', 'grosir', 'karpet',
        'sosis', 'salon', 'skin', 'care', 'cloth', 'tech', 'rental', 'kamera',
        'beauty', 'express', 'kredit', 'collection', 'impor', 'preloved',
        'follow', 'follower', 'gain', '.id', '_id', 'bags'
    ],
    unfollow_whitelist=['example_user_1', 'example_user_2'])
while True:

    # print("# MODE 0 = ORIGINAL MODE BY LEVPASHA")
    # print("## MODE 1 = MODIFIED MODE BY KEMONG")
    # print("### MODE 2 = ORIGINAL MODE + UNFOLLOW WHO DON'T FOLLOW BACK")
    # print("#### MODE 3 = MODIFIED MODE : UNFOLLOW USERS WHO DON'T FOLLOW YOU BASED ON RECENT FEED")
    # print("##### MODE 4 = MODIFIED MODE : FOLLOW USERS BASED ON RECENT FEED ONLY")
    # print("###### MODE 5 = MODIFIED MODE : JUST UNFOLLOW EVERYBODY, EITHER YOUR FOLLOWER OR NOT")

    ################################
    ##  WARNING   ###
    ################################

    # DON'T USE MODE 5 FOR A LONG PERIOD. YOU RISK YOUR ACCOUNT FROM GETTING BANNED
    # USE MODE 5 IN BURST MODE, USE IT TO UNFOLLOW PEOPLE AS MANY AS YOU WANT IN SHORT TIME PERIOD

    mode = 0

    # print("You choose mode : %i" %(mode))
    # print("CTRL + C to cancel this operation or wait 30 seconds to start")
    # time.sleep(30)

    if mode == 0:
        bot.new_auto_mod()

    elif mode == 1:
        check_status(bot)
        while bot.self_following - bot.self_follower > 200:
            unfollow_protocol(bot)
            time.sleep(10 * 60)
            check_status(bot)
        while bot.self_following - bot.self_follower < 400:
            while len(bot.user_info_list) < 50:
                feed_scanner(bot)
                time.sleep(5 * 60)
                follow_protocol(bot)
                time.sleep(10 * 60)
                check_status(bot)

    elif mode == 2:
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3:
        bot.bot_mode = 3
        while(bot.login_status == 1):
            bot.unfollow_recent_feed()
            time.sleep(5)

    elif mode == 4:
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 5:
        bot.bot_mode = 2
        unfollow_protocol(bot)

    else:
        print("Wrong mode!")
=======
"""
The example.py is deprecated. Please use the declarative mode with YAML settings
Please refer to Github README + (instabot -h) + Blog section for further information
"""
print(__doc__)
>>>>>>> upstream_master
