import './App.css';
import Custombutton1 from './components/custombutton1';
import { createTheme, ThemeProvider} from '@material-ui/core/styles';
import { TextField } from '@material-ui/core';
import Typical from 'react-typical'
import { useState } from 'react';
import logo from './cs124logo.png';

const theme = createTheme({
  palette: {
    primary: {
      main:"#2e1667",
    },
    secondary: {
      main:"#c7d8ed",
    },
  },
  typography: {
    fontFamily: [
      'Roboto'
    ],
    h4: {
      fontWeight: 600,
      fontSize: 28,
      lineHeight: '2rem',
      },
    h5: {
      fontWeight: 100,
      lineHeight: '2rem',
    },
  },
})

// Prompt
// Artist
// Genre
// Mood
// Number of songs (Any of the fields may be left blank)

function App() {
  const [paragraphText, setParagraphText] = useState(''); // Initial state is argument passed

  return (
    <div style={{
      
    }}>
      <ThemeProvider theme={theme}>
        <p style={{
          fontSize: 30,
          marginLeft: '33%',
        }}>Welcome to Group 38's{' '}
          {<Typical loop={Infinity} wrapper="b" steps={[
            'song-writing AI', 2500,
            'lyric generator', 2500,
            'neural network', 2000,
            'final project', 2500,
            'last minute scramble', 1500,
          ]}>
          </Typical>}
        </p>
      </ThemeProvider>
      <div style={{
        marginLeft: "30%",
        paddingBottom: '50px'
      }}>
        <TextField id="standard-basic" label="Artist" variant="standard" style={{
          paddingRight: '25px'
        }}/>
        <TextField id="standard-basic" label="Genre" variant="standard" style={{
          paddingRight: '25px'
        }}/>
        <TextField id="standard-basic" label="Mood" variant="standard" style={{
          paddingRight: '25px'
        }}/>
      </div>
      <div style={{
        marginLeft: '45%'
      }}>
        <TextField id="outlined-basic" label="Prompt" variant="outlined" multiline/>
      </div>
      <div onClick={() => setParagraphText("Uh huh, yuh yuh yuh ayy") } style={{
        marginLeft: '47.5%',
        marginTop: '2%'
      }}>
        <Custombutton1 txt="Generate Song"/>
      </div>
      <p style={{
        width: '50%',
        height: '300px',
        marginLeft: '45%',
        marginTop: '60px',
        alignContent: 'center',
        border: '3px solid navy'
      }}>{paragraphText}</p>
      <div class='box'>
        <div class='wave -one'></div>
        <div class='wave -two'></div>
        <div class='wave -three'></div>
      </div>
    </div>
  );
}

export default App;
