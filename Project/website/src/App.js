import logo from './logo.svg';
import './App.css';
import Custombutton1 from './components/custombutton1';
import { createTheme, ThemeProvider} from '@material-ui/core/styles';

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

function App() {
  return (
    <div className="App" style={{
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center'
    }}>
      <ThemeProvider theme={theme}>
        <Custombutton1 txt="Generate Lyrics"/>
      </ThemeProvider>
    </div>
  );
}

export default App;
