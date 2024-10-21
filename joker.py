import hashlib

user = input("Enter the address: ") 


user = user.replace(" ", "")
user = user.lower()
user = hashlib.sha256(user.encode()).hexdigest()


if user == '2d9e0b5374ef3727c47bb0288e71e07334a98b4356f1b6ed8657981f01946a28':
    print("Check out this cool repo: https://github.com/torvalds/linux")
elif user == 'a6c4df6f8f8c02b678e5c17e9cbdb6a34b3eec2e5150c99bc7be3966b43f7887':
    print("Explore this repo: https://github.com/microsoft/vscode")
elif user == 'c4b775cc1d47d13ab38a9305d7583026871c17946cfdf129c489f2d4f2673f8a':
    print("Take a look at: https://github.com/tensorflow/tensorflow")
elif user == '18e0e3b8f2b5dfd1c9244fa418d2d8e4170159d0c64aa0b6e7b1f4f8b87fd87d':
    print("Explore this: https://github.com/psf/requests")
elif user == '498845f48b54d58e86ba7a7484b6d9e80b0ff8d2b2453cbca25baeb8d909d7d7':
    print("Check this out: https://github.com/django/django")
elif user == '4d8f805e9cc3af35b2e63fe9b7b0959c8c7a29f089650d43f2725d1d103c1fcf':
    print("Here's something interesting: https://github.com/keras-team/keras")
elif user == '76041a4aef3b91e9e2c9f067c13eb97223d282fb474a8c57ab8178858077d49b':
    print("Interesting project: https://github.com/vuejs/vue")
elif user == '5c68e2b0a9b61cc42c35a95f8e54c4c07c59387bce301a99c355872c9c5a25e4':
    print("Discover this repo: https://github.com/flask-admin/flask-admin")
elif user == 'd83fda1b37d6e85d1c4849d24d91c7dc674b0b3a85c5a8fc44b6ad1b2825f1c1':
    print("Check it out: https://github.com/kubernetes/kubernetes")
elif user == '8938d0a17d82f33eb7999dbfe7e3348343e15a7a0457dfc2e9b256d8d1034a85':
    print("Explore this cool repo: https://github.com/facebook/react")
elif user == 'ba6e1cba99ad564d785c781aef77d93e53f37d7ea834b17415656c21b73092d4':
    print("Take a look at: https://github.com/apache/spark")
elif user == 'ab5e1e1c6bb947e5dbe155f2b0f7fa9b9bb5758e1bbf51d45373472656b43198':
    print("Great repo here: https://github.com/numpy/numpy")
elif user == '32c394007c13d376d9577de1f8fefaf92bc5e9a1d1df9a8a78057ea68d8b9d58':
    print("Find something cool: https://github.com/pallets/flask")
elif user == 'edcb23bff4ebff9a3be7e26cbf99b5471b0cf15c5c2b79e91c98d8e3a0b31342':
    print("Check this out: https://github.com/rust-lang/rust")
elif user == 'c16d40acb863edb2ffc043c0e64a810b92493002e9dbac229d34312f5acf5d99':
    print("Great find: https://github.com/he1senbrg/ml4s-dots")
elif user == '82a2482fe0c54e5c61a117c49f80e84c612db8ab3c7e4c21be2493566a9f8f31':
    print("Explore more here: https://github.com/sveltejs/svelte")
elif user == '8f530a5781e3fa3a0ba2c42df9f53edb5cf2c089bb45b52f1f3f5a7baf81e3f5':
    print("Interesting repo: https://github.com/apache/kafka")
elif user == 'a12e83d4f92f7d747a789edce23fb1da7351f93e9a0b7138538913e04c221fe2':
    print("Check this out: https://github.com/pytorch/pytorch")
elif user == '73c0fa793a3fb637dd0d2a93988cb57f934712feea65383cbef22f56f0429e2b':
    print("Explore this: https://github.com/tiangolo/fastapi")
elif user == 'fa25c8da50fcf25f8f86556f6e5cb741b949087b90d871cd36f6e0b4ff3f86ea':
    print("Check it out: https://github.com/scikit-learn/scikit-learn")
elif user == '72bc6c2882e97023532fcd6d914a24f63dba6006fd79a5d5a6bef9e5ba352d2f':
    print("Interesting repo: https://github.com/Drone944/pysocks")  # Updated repo link
elif user == '7b17b9ef62103b850236d5d509f11e396e3a246b08f45f0dcce70f31392e0e91':
    print("Great find: https://github.com/elastic/elasticsearch")
elif user == 'c3be39b3ec6e64b4179b3033a72d4693dfc3c743c120d47931970e1b8fffc88e':
    print("Discover this repo: https://github.com/ansible/ansible")
elif user == '58934e27a504bc52bb7413ffcd69d04a7a5c172f6c83ff627be8c7838ff27863':
    print("Cool repo: https://github.com/git/git")
elif user == '61374167cc68a0047b36ad10f85f2912ff923bc83db6b9e038a26f89e2851234':
    print("Interesting project: https://github.com/gnachman/iTerm2")
elif user == '1b96784a5dfecae6cf1f17f24b40b3e19c3679e660e01766aa46c81f37b9b367':
    print("Explore this: https://github.com/goharbor/harbor")
elif user == '5bba2325a0178b0ea905efba39250ac87f4f2bfc1ef01b702f7ad4b85f47fa10':
    print("Find more here: https://github.com/puppeteer/puppeteer")
elif user == 'c6eab2c8f595ed67d7a4b383b883f9947a67e274544d66c204d2f9e6cbca0e6d':
    print("Explore this cool project: https://github.com/mozilla/pdf.js")
elif user == 'fa2d47956cd6ab222af905ba93d4a7605ea60de7f1f3509b074e6b1bff3f291a':
    print("Discover this repo: https://github.com/atom/atom")
elif user == '2f52abcb4f27853ab7a97127b4d989991efdbbc27111b571fb3bfe2a8c3e6c3d':
    print("Interesting project: https://github.com/huggingface/transformers")
elif user == 'd72df1d7f83a94d89ff82b8395db8a77ef0e3c14d30913b85aa38a7be2648b0f':
    print("Check this repo out: https://github.com/nvim-treesitter/nvim-treesitter")
elif user == 'f3611f2dd83a59fdf885d024b4c91c88f580a656d763ae4ebfb7e7937cbb3d77':
    print("Great repo: https://github.com/alacritty/alacritty")
else:
    print("Unknown user or no repo associated.")

