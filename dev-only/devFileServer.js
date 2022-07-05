import express from 'express';
import cors from 'cors';
import morgan from 'morgan';

const app = express();
const PORT = process.env.PORT || 5001;

// Morgan logger
app.use(morgan('tiny'));

// Middleware
app.use(cors());
app.use(express.json()); // based on body parser
app.use(express.urlencoded({ extended: true }));

app.get('/file', (req, res) => {
  const path = req.query.path;
  if(!path) {
    res.sendStatus(404);
  }

  res.sendFile(path);
});

app.get('/test', (req, res) => {
  res.send(`Server is running on port ${PORT}`);
});

app.listen(PORT, (err) => {
  if(err) console.error(err);
  console.log(`Success! Your application is running on port ${PORT}`);
});
