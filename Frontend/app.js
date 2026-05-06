const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();

app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));

app.get('/', (req, res) => {
    res.render('index', { response: null });
});

app.post('/submit', async (req, res) => {

    const formData = {
        name: req.body.name,
        email: req.body.email,
        message: req.body.message
    };

    try {

        const response = await axios.post(
            'http://backend:5000/submit',
            formData
        );

        res.render('index', {
            response: response.data.message
        });

    } catch (error) {

        res.render('index', {
            response: 'Error connecting to backend'
        });
    }
});

app.listen(3000, () => {
    console.log('Frontend running on port 3000');
});