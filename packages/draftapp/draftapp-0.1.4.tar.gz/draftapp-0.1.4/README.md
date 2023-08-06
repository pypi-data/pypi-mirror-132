<div id="top"></div>

<!-- Shields here -->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ratanboddu/draftapp">
    <img src="images/logo.png" alt="DraftApp" width="100" height="100">
  </a>

  <h3 align="center">DraftApp</h3>

  <p align="center">
    Build scalable production-grade web applications within seconds<br />
    <br />
    <a href="https://github.com/ratanboddu/draftapp"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ratanboddu/draftapp/issues">Report Bug</a>
    ·
    <a href="https://github.com/ratanboddu/draftapp/issues">Request Feature</a>
  </p>
</div><br />

Getting Started
------------
It is recommended to install DraftApp (and your project's other dependencies) in a virtualenv.

Once you’ve created and activated your Python virtual environment, you can install the latest stable release of DraftApp into this dedicated development workspace:

```
pip install draftapp
```


<p align="right">(<a href="#top">back to top</a>)</p>



Set Up a DraftApp project
------------
After you’ve successfully installed DraftApp, you’re ready to create the first draft for your new web application

You can choose from one of the two types:

* A **Basic** App provides you with the basic scaffold needed to get you application up and running for development
* An **Advanced** App provides you with a high-level scaffold for your development needs with Docker, Kubernetes manifests & Code Obfuscation


### Frameworks

To check the available frameworks to set up your application with,

  ```sh
   draftapp --help
   ```
   
### Tyeps

To check the available types for the frameworks to set up your application with,

  ```sh
   draftapp flask --help
   ```
   
### Basic Flask Application

To set up a basic Flask Application,

  ```sh
   draftapp flask -t basic -n portfolio -d /tmp/Portfolio
   ```
#### Tree Structure for Basic Flask Application
  ```sh
   Portfolio/
├── Makefile
├── README.md
├── alembic
│   ├── README
│   ├── env.py
│   └── script.py.mako
├── alembic.ini
├── bin
│   └── portfolio-cli
├── configs
│   ├── gunicorn.py
│   └── local.ini
├── logs
│   └── app.log
├── portfolio
│   ├── __init__.py
│   ├── config.py
│   ├── constants.py
│   ├── manager.py
│   ├── models.py
│   ├── schemas.py
│   ├── swag
│   │   └── ping.yaml
│   └── views.py
└── setup.py
   ```

### Advanced Flask Application

To set up an advanced Flask Application,

  ```sh
   draftapp flask -t advanced -n portfolio -d /tmp/Portfolio
   ```
#### Tree Structure for Advanced Flask Application
  ```sh
  Portfolio
├── Dockerfile
├── Makefile
├── README.md
├── alembic
│   ├── README
│   ├── env.py
│   └── script.py.mako
├── alembic.ini
├── bin
│   └── portfolio-cli
├── compile.py
├── configs
│   ├── gunicorn.py
│   ├── local.ini
│   └── test.ini
├── kubernetes_manifests
│   ├── README.md
│   ├── configmap.yaml
│   ├── deployment.yaml
│   ├── hpa.yaml
│   ├── ingress.yaml
│   └── service.yaml
├── lint.py
├── logs
│   └── app.log
├── portfolio
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── config.cpython-36.pyc
│   │   ├── manager.cpython-36.pyc
│   │   └── views.cpython-36.pyc
│   ├── config.py
│   ├── constants.py
│   ├── exceptions.py
│   ├── log.py
│   ├── manager.py
│   ├── middlewares.py
│   ├── models.py
│   ├── schemas.py
│   ├── swag
│   │   └── ping.yaml
│   ├── utils.py
│   ├── validators.py
│   └── views.py
├── portfolio.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   ├── requires.txt
│   └── top_level.txt
├── pytest.ini
├── setup.py
└── tests
    ├── __init__.py
    ├── conftest.py
    └── test_views.py
  ```


  

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [ ] Add Documentation (readthedocs)
- [ ] Add docker-compose for Advanced option
- [ ] Add Additional Python Frameworks
- [ ] Add examples

See the [open issues](https://github.com/ratanboddu/draftapp/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/new-feature`)
3. Commit your Changes (`git commit -m 'Added new feature'`)
4. Push to the Branch (`git push origin feature/new-feature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Django](https://www.djangoproject.com/)
* [Img Shields](https://shields.io)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#top">back to top</a>)</p>
