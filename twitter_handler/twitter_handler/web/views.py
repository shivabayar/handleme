from django.shortcuts import render
import twitter


def get_index_page(request):
    api = twitter.Api(consumer_key='YM7lZLIwUlaKh70kcMFuodMQl',
                      consumer_secret='bsFtG0RVgaSlYkVUy3at99JuIdOdtsfRpVWf4SBbxII0yK0zyK',
                      access_token_key='391498643-YrBYllBegsfTSPYslZHLpg86FiAsiFLTfd2HLDF7',
                      access_token_secret='LgAQ8qP3XFRJX4vfauxKr0SB1QHm3ZonKyZSoBuFLI79R')

    timeline = api.GetUserTimeline(screen_name='iamsrk', exclude_replies=False, include_rts=True)
    # followers = api.GetFollowers(screen_name='shiva_bayar', count=10, include_user_entities=False)

    for time in timeline:
        print time.text

    # for follower in followers:
    #     print follower

    return render(request, 'index.html')
