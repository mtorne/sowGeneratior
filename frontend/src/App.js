import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';

function App() {
  const [cliente, setCliente] = useState('');
  const [proyecto, setProyecto] = useState('');
  const [servicios, setServicios] = useState('');
  const [descripcionValidacion, setDescripcionValidacion] = useState('');
  const [loading, setLoading] = useState(false);
  const [markdownPreview, setMarkdownPreview] = useState('');

  const handleGenerar = async (e) => {
    e.preventDefault();
    setLoading(true);
    setMarkdownPreview('');

    try {
      const response = await fetch('http://89.168.92.241:8000/generarmd', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          cliente,
          proyecto,
          servicios_oci: servicios.split(',').map(s => s.trim()),
          descripcion_validacion: descripcionValidacion
        })
      });

      if (!response.ok) {
        throw new Error('Error generando el contenido');
      }

      const markdownText = await response.text(); // Asumimos que el backend responde con Markdown
      setMarkdownPreview(markdownText);
    } catch (error) {
      alert(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '800px', margin: '40px auto', fontFamily: 'Arial', padding: '20px' }}>
      <h1 style={{ color: '#333', textAlign: 'center' }}>Generador de Documento Técnico (OCI)</h1>
      
      <form onSubmit={handleGenerar} style={{ background: '#f9f9f9', padding: '20px', borderRadius: '8px' }}>
        <div style={{ marginBottom: '15px' }}>
          <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>Cliente:</label>
          <input 
            value={cliente} 
            onChange={e => setCliente(e.target.value)} 
            required 
            style={{ width: '100%', padding: '8px', borderRadius: '4px', border: '1px solid #ddd' }}
          />
        </div>

        <div style={{ marginBottom: '15px' }}>
          <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>Proyecto:</label>
          <input 
            value={proyecto} 
            onChange={e => setProyecto(e.target.value)} 
            required 
            style={{ width: '100%', padding: '8px', borderRadius: '4px', border: '1px solid #ddd' }}
          />
        </div>

        <div style={{ marginBottom: '15px' }}>
          <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>
            Servicios OCI (separados por coma):
          </label>
          <input 
            value={servicios} 
            onChange={e => setServicios(e.target.value)} 
            required 
            style={{ width: '100%', padding: '8px', borderRadius: '4px', border: '1px solid #ddd' }}
            placeholder="Ej: Compute, Autonomous Database, VCN"
          />
        </div>

        <div style={{ marginBottom: '20px' }}>
          <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>
            Descripción de Validación:
          </label>
          <textarea 
            value={descripcionValidacion} 
            onChange={e => setDescripcionValidacion(e.target.value)} 
            required 
            style={{ 
              width: '100%', 
              padding: '8px', 
              borderRadius: '4px', 
              border: '1px solid #ddd',
              minHeight: '100px'
            }}
            placeholder="Objetivos, alcance y criterios de éxito de la validación"
          />
        </div>

        <button 
          type="submit" 
          disabled={loading}
          style={{
            background: '#007bff',
            color: 'white',
            padding: '10px 15px',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer',
            fontSize: '16px',
            width: '100%',
            opacity: loading ? 0.7 : 1
          }}
        >
          {loading ? 'Generando Vista Previa...' : 'Generar Vista Previa'}
        </button>
      </form>

      {markdownPreview && (
        <div style={{ marginTop: '40px', padding: '20px', background: '#fff', border: '1px solid #ccc', borderRadius: '8px' }}>
          <h2>Vista Previa del Documento</h2>
          <ReactMarkdown>{markdownPreview}</ReactMarkdown>
        </div>
      )}
    </div>
  );
}

export default App;

