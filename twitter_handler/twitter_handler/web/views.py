from django.shortcuts import render, render_to_response
import twitter
from rest_framework.views import APIView
from setuptools.command import register

api = twitter.Api(consumer_key='YM7lZLIwUlaKh70kcMFuodMQl',
                  consumer_secret='bsFtG0RVgaSlYkVUy3at99JuIdOdtsfRpVWf4SBbxII0yK0zyK',
                  access_token_key='391498643-YrBYllBegsfTSPYslZHLpg86FiAsiFLTfd2HLDF7',
                  access_token_secret='LgAQ8qP3XFRJX4vfauxKr0SB1QHm3ZonKyZSoBuFLI79R')


def get_index_page(request):
    # print "len:" + str(len(timeline))
    # tweets = api.GetFavorites(user_id='2597413135', screen_name='RashtrapatiBhvn', include_entities=True, count=1000,
    #                           since_id=1)
    # print len(tweets)
    # for tweet in tweets:
    #     print tweet.text
    #     print '--------'

    # for time in timeline:
    #     print time.text
    #     print '--------'
    # print time.id

    # for follower in followers:
    #     print follower

    return render(request, 'search-box.html')


class UserViewSet(APIView):
    def get(self, request, handler):
        timeline = api.GetUserTimeline(screen_name=handler, exclude_replies=False,
                                       include_rts=True, count=10)

        if len(timeline) > 0:
            profile_pic = str(timeline[0].user.profile_image_url)
            profile_pic = profile_pic.replace("normal", "200x200")
            name = timeline[0].user.name
            profile_url = timeline[0].user.url
            banner_url = timeline[0].user.profile_banner_url

            import pdb
            pdb.set_trace()

            response_dict = {'handler': handler,
                             'profile_pic': profile_pic,
                             'name': name,
                             'profile_url': profile_url,
                             'banner_url': banner_url,
                             'timeline': timeline,
                             'timeline_len': len(timeline)}
            return render(request, 'search-result.html', response_dict)
        else:
            return render(request, 'data-not-found.html', {})
