// import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.tsx'
import './index.css'
// import { Something } from './urvashi.tsx'

createRoot(document.getElementById('root')!).render(
  // <StrictMode>
    <App />
    // <Something />
  // </StrictMode>,
)
