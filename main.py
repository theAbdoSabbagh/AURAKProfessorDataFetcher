from internal.fetcher import Fetcher

if __name__ == "__main__":
    fetcher = Fetcher()
    fetcher.run()
    fetcher.display_professors()
    fetcher.save_professors()
