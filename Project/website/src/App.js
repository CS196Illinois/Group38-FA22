import logo from './logo.svg';
import './App.css';
import Custombutton1 from './components/custombutton1';
import { createTheme, ThemeProvider} from '@material-ui/core/styles';
import Typical from 'react-typical'

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

// Generate Lyrics button
// Buttons to choose a style
// Text box to input a prompt
// Title that welcomes users to the page
// Animation at bottom of screen, or nice background
// Paragraph that changes based on the generated lyrics
function App() {
  return (
    <div style={{
      display: 'flex',
      justifyContent: 'center',
      backgroundColor: 'lavender'
    }}>
      <ThemeProvider theme={theme}>
        <p>Welcome to Group 38's{' '}
          <Typical loop={Infinity} wrapper="b" steps={[
            'song-writing AI', 1500,
            'lyric generator', 1500,
            'neural network', 1500,
            'final project', 1500,
            'last minute scramble', 1500,
          ]}>
          </Typical>
        </p>
        <Custombutton1 txt="Generate Lyrics"/>
      </ThemeProvider>
    </div>
  );
}

export default App;
