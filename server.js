const express = require('express');
const bodyParser = require('body-parser');
const nodemailer = require('nodemailer');

const app = express();
app.use(bodyParser.json());

app.use(express.static(__dirname));

app.post('/send-email', async (req, res) => {
  const { username, email, password } = req.body;

  const transporter = nodemailer.createTransport({
    service: 'Gmail',
    auth: {
      user: 'vica.ti17@gmail.com', // Ваш Gmail адрес
      pass: 'IamGroot10' // Пароль от вашего Gmail аккаунта
    }
  });

  const mailOptions = {
    from: 'vica.ti17@gmail.com',
    to: email,
    subject: 'Hello',
    text: 'Hello, ' + username + '! Welcome to our website!'
  };

  try {
    await transporter.sendMail(mailOptions);
    res.json({ message: 'Message sent successfully.' });
  } catch (error) {
    console.error('Error sending email:', error);
    res.status(500).json({ message: 'An error occurred while sending the email.' });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
