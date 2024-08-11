<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/VDF1OSb.png" alt="Project logo"></a>
</p>

<h3 align="center">Derm IQ</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/seun-beta/derm-iq-backend.svg)](https://github.com/seun-beta/derm-iq-backend/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/seun-beta/derm-iq-backend.svg)](https://github.com/seun-beta/derm-iq-backend/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center">Derm IQ is a comprehensive skincare e-commerce platform powered by FastAPI and MongoDB, offering personalized skincare product recommendations using OpenAI's GPT model.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [File Structure](#file_structure)
- [TODO](#todo)
- [Contributing](#contributing)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

**Derm IQ** is designed to enhance the online skincare shopping experience by providing personalized product recommendations based on users' skincare needs. The platform allows users to browse through a curated collection of skincare products, add them to their cart, and place orders seamlessly. With an integration of OpenAI's GPT model, users receive tailored skincare advice, ensuring they find the best products for their skin type and concerns.

## 🏁 Getting Started <a name = "getting_started"></a>

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following software installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- An OpenAI API Key (Sign up at [OpenAI](https://beta.openai.com/signup/))

### Installing

1. **Clone the repository:**

   ```bash
   git clone https://github.com/seun-beta/derm-iq-backend.git
   cd derm-iq-backend
   ```

2. **Create a `.env` file in the root directory:**

   ```env
   OPENAI_API_KEY=your_openai_api_key
   JWT_ALGORITHM=HS256
   JWT_SECRET=your_jwt_secret
   JWT_ACCESS_TOKEN_EXP_MINUTES=30
   ```

3. **Build and start the Docker containers:**

   ```bash
   docker-compose up --build
   ```

4. **Access the application:**

   The application will be running at `http://localhost:8000`.

## 🎈 Usage <a name="usage"></a>

Once the application is running, you can:

- **Register/Login**: Access the authentication endpoints to create an account or log in.
- **Browse Products**: Use the `/products/list-products` endpoint to view all available products.
- **Get Recommendations**: Submit a skincare questionnaire to the `/products/recommend` endpoint and receive personalized recommendations.
- **Add to Cart**: Add recommended products to your cart and place orders using the `/orders` endpoints.

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Programming Language
- [FastAPI](https://fastapi.tiangolo.com/) - Web Framework
- [MongoDB](https://www.mongodb.com/) - Database
- [Docker](https://www.docker.com/) - Containerization
- [OpenAI GPT](https://openai.com/) - AI Model

## 🗂️ File Structure <a name = "file_structure"></a>

```
.
├── app
│   ├── config.py             # Configuration settings
│   ├── users
│   │   ├── models.py         # User model
│   │   ├── routers.py        # User authentication routes
│   ├── products
│   │   ├── models.py         # Product model
│   │   ├── routers.py        # Product routes
│   │   ├── schemas.py        # Product schemas
│   ├── orders
│   │   ├── models.py         # Order and CartItem models
│   │   ├── routers.py        # Order routes
│   │   ├── schemas.py        # Order schemas
├── Dockerfile                # Dockerfile for FastAPI app
├── docker-compose.yml        # Docker Compose file
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables
└── README.md                 # Project documentation
```

## 🤝 Contributing <a name = "contributing"></a>

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/seun-beta/derm-iq-backend/issues).

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a pull request

## ✍️ Authors <a name = "authors"></a>

- [@seun-beta](https://github.com/seun-beta) - Idea & Initial work

See also the list of [contributors](https://github.com/seun-beta/derm-iq-backend/contributors) who participated in this project.

## 🎉 Acknowledgments <a name = "acknowledgement"></a>

- Thanks to the FastAPI community for their invaluable documentation.
- Inspiration from modern e-commerce solutions and personalized recommendation engines.
- Special thanks to anyone whose contributions or code snippets were used in this project.
