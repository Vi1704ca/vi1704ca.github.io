const express = require('express');
const bodyParser = require('body-parser');
const nodemailer = require('nodemailer');

const app = express();
app.use(bodyParser.json());

app.use(express.static(__dirname));

app.post('/send-email', async (req, res) => {
  const { name, email, message } = req.body;

  const transporter = nodemailer.createTransport({
    service: 'Gmail',
    auth: {
      user: 'your@gmail.com', // Ваш Gmail адрес
      pass: 'your_password' // Пароль от вашего Gmail аккаунта
    }
  });

  const mailOptions = {
    from: '"Кевин" <your@gmail.com>',
    to: email,
    subject: 'Hello',
    text: `Hello, ${name}!\n\nWelcome to our website!\n\nMessage: ${message}`
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
