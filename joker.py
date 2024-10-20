import hashlib


user = int(input("Enter the address: "))


#There is a small error in the above line of this code. Fix it to run it successfully
# Maybe go through the 'data type' of values that are compared to 'user' and make the small change in the above line.

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
    print("Great find : https://github.com/he1senbrg/ml4s-dots")
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
    print("Interesting repo: https://github.com/he1senbrg/cyberML")
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
elif user == 'c4e84d647e2fbc531993b07b0897517853ba08ad53a8f8d0b7f0f2185a9fa59e':
    print("Great find: https://github.com/prometheus/prometheus")
elif user == '11b3853e591c8a9b4232bc1a4f7ff47f49fa17293d8f7a6d9eb221b7b52315bb':
    print("Cool project: https://github.com/openai/gym")
elif user == 'ac85e1a57fa79543d76d15f4f9e1fa0a18b0f4d4c135a67cfb0ed1722345d6e2':
    print("Find more here: https://github.com/apache/superset")
elif user == '2a47db9a4f0bfcfca616a02e755c0264b43cf5175c768803b8c8031aa1394f8f':
    print("Interesting repo: https://github.com/matplotlib/matplotlib")
elif user == '74f7edb6db3b435b82e295998672925321a164b92f70547fbde83bb4bfa33a5e':
    print("Great discovery: https://github.com/apache/flink")
elif user == '20ae3e88c4b7c28b55560e51c0f7e0b11fd3df703a4d1d97f23b12b84dce4a4a':
    print("Discover more here: https://github.com/celery/celery")
elif user == '73e5d84a37eb074e2a2cb6c45034fe12860120436bb34b13a61c4b57b2537c92':
    print("Interesting find: https://github.com/urllib3/urllib3")
elif user == '74e33f73ec4a889b5a6c4e4a3db7ef846ed07ddae9e08688b7a2957fc75c137a':
    print("Check this project out: https://github.com/tesseract-ocr/tesseract")
elif user == '45f3dbf1a1dfce094c4722367885e3539b73e3c38b5d84dfc9f0339ba7f9a38d':
    print("Explore this repo: https://github.com/nltk/nltk")
elif user == 'db4b8e87b9fda74f7dcd1778e65aab76b54b123a2fd2ad7a5a9fb3e934adbe21':
    print("Discover this: https://github.com/expressjs/express")
elif user == '3ed1b963eb63b3edb6f453fba16406f9f8d2c26f9e7f6cc4b25d0a72a00d2e99':
    print("Cool find: https://github.com/sinonjs/sinon")
elif user == '7ab54d39b7b9edce17e63c1f5f61a7b9fda5d6fd3711744d489dce9c51c69ef4':
    print("Check it out: https://github.com/graphql/graphql-js")
elif user == '6f93c2d71a52bc0632b4b8a1bba8b5f595ce68d52cde6f739f74657d1950edab':
    print("Cool discovery: https://github.com/graphene-python/graphene")
elif user == 'cc6e2268f85e8eaf5aead5f43be4996e0f6fba0be330cf82759b802897d8bfff':
    print("Great project: https://github.com/ovh/manager")
elif user == 'eef91d236dfda7be93baf3bb3b41af9922fafe7d70f29a3d29bc7997a33b2c48':
    print("Explore this repo: https://github.com/chakra-ui/chakra-ui")
elif user == 'eefdfb05e4f89141fa1237bbdaf9f43a712e4f5b0c3700cfde93d1b3efede3b6':
    print("Interesting project: https://github.com/DefinitelyTyped/DefinitelyTyped")
elif user == 'bdfa3e43d9d8c87ac7e743ed3760ab88c3eaed4e35d63c82918c7ba17f378b5d':
    print("Check it out: https://github.com/rancher/rancher")
elif user == 'd16e6d2e4d2fa9fdf5ae7413cb75000bc0322c09341dc9e9f85d9b7d1ba614d8':
    print("Explore this repo: https://github.com/openai/spinningup")
elif user == '00dba4c41a7f234b3c6fe93cccd66da0f179c1f8f70bbd4cf981ebfc9e50c71a':
    print("Check it out: https://github.com/apache/beam")
elif user == '31303aafc479b2dfe0b35de25c5fbbe2badddb3f51f594f989c0f6c4ef30abbb':
    print("Discover this repo: https://github.com/postmanlabs/postman-app-support")
elif user == 'd7b3db08b5f8887e40e4979f3791d76823696d493a4fe8728e12a9fcf55fb57b':
    print("Great find: https://github.com/fenics-project/fenics")
elif user == '9d34418b5674fa35a5ad35ad7550adacb52f22bb17e084a5d9c21e78f112bf71':
    print("Interesting repo: https://github.com/redwoodjs/redwood")
elif user == 'ee68a3cbdf57a06e2f7d1279af5e1f54ae2e5a2b0f7c2b8bdf72d52f03cfc5d4':
    print("Explore more: https://github.com/apache/arrow")
elif user == 'f445edb9829f2bb913bd94b8f7d2562a18f9879e49187fb0fe6695950c34e0c4':
    print("Check it out: https://github.com/moby/moby")
elif user == '37ce32e7a4b27ef90ef8367d6036747e58f5f05f2dd3d74fcf45247fa7d530b9':
    print("Cool project: https://github.com/ziglang/zig")
elif user == 'a8d57e0d98eb3ab7687b70f1c8e20bbaebbbcc3c9f5a756d3ae4dfb7d6221d93':
    print("Discover this repo: https://github.com/iterative/dvc")
elif user == '6c83a88b4fd418acdb8edbe041c9d2030fd9e1e3cdd85c09f3b9df5dc3674d0b':
    print("Interesting project: https://github.com/fishtown-analytics/dbt")
elif user == '8e3ef1b0fc1f7c4f6b53b6a530732db3fbbd2ae4c5f4d477afba4b45ab60b073':
    print("Explore this repo: https://github.com/boostorg/boost")
elif user == '582dff46e1b9f3b1e38ebf1deed09ae0a2d91f038c6163aee4c3abf4c1d3b58b':
    print("Check it out: https://github.com/erlang/otp")
elif user == '8e31dbd5b46fd1eaf7d0f11ba92bfc68db30af91b264fb88819133ad7a1671b8':
    print("Cool discovery: https://github.com/strapi/strapi")
elif user == '58683e7747bb8308e2adf86b7639ae6e3ac95377c8a118a09178a2b9f732b071':
    print("Great project: https://github.com/bitnami/charts")
else:
    print("No match found. Keep exploring GitHub repos!")

