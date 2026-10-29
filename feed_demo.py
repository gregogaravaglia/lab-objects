"""A small social feed for skaters at Center Ice in Ontario, California."""

from lab_classes import User, Tweet


def build_feed():
    """Create rink accounts and posts, then record a little activity."""
    users = [User('grego_skates'), User('greg_on_ice')]
    posts = [
        Tweet('grego_skates', 'Getting some extra practice in at center ice tonight. #CenterIce'),
        Tweet('greg_on_ice', 'Anyone else going to public session this weekend???'),
        Tweet('grego_skates', 'I finally landed that turn without losing my balance #ate'),
    ]

    users[0].follow()
    users[1].follow()
    users[0].unfollow()

    posts[0].like()
    posts[1].like()
    posts[1].unlike()

    return users, posts


def main():
    """Print the accounts and posts in the feed."""
    users, posts = build_feed()

    print('Center Ice Community')
    print('\nAccounts')
    for user in users:
        print(user)

    print('\nPosts')
    for post in posts:
        print(post)
        print('Hashtags:', post.hashtags())


if __name__ == '__main__':
    main()
