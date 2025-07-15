import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

function App() {
  const [cliente, setCliente] = useState('');
  const [proyecto, setProyecto] = useState('');
  const [servicios, setServicios] = useState('');
  const [descripcionValidacion, setDescripcionValidacion] = useState('');
  const [loading, setLoading] = useState(false);
  const [previewContent, setPreviewContent] = useState('');

  const handleGenerar = async (e) => {
    e.preventDefault();
    setLoading(true);

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
        throw new Error('Error generando el documento');
      }

      const markdown = await response.text();
      setPreviewContent(markdown);
    } catch (error) {
      alert(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '800px', margin: '40px auto', fontFamily: 'Arial', padding: '20px' }}>
      <h1 style={{ color: '#333', textAlign: 'center' }}>Labs SoW Generator - Application Validation (OCI)</h1>
      <form onSubmit={handleGenerar} style={{ background: '#f9f9f9', padding: '20px', borderRadius: '8px' }}>
        <div style={{ marginBottom: '15px' }}>
          <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>Customer:</label>
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
            OCI Services (comma separated):
          </label>
          <input
            value={servicios}
            onChange={e => setServicios(e.target.value)}
            required
            placeholder="Ej: Compute, Autonomous Database, VCN"
            style={{ width: '100%', padding: '8px', borderRadius: '4px', border: '1px solid #ddd' }}
          />
        </div>

        <div style={{ marginBottom: '20px' }}>
          <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>
            Project Description:
          </label>
          <textarea
            value={descripcionValidacion}
            onChange={e => setDescripcionValidacion(e.target.value)}
            required
            placeholder="Objetivos, alcance y criterios de éxito de la validación"
            style={{
              width: '100%',
              padding: '8px',
              borderRadius: '4px',
              border: '1px solid #ddd',
              minHeight: '100px'
            }}
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
          {loading ? 'Generating Markdown...' : 'Generate Markdown'}
        </button>
      </form>

      {previewContent && (
        <div style={{ marginTop: '40px', background: '#fff', padding: '20px', borderRadius: '8px', border: '1px solid #ddd' }}>
          <h2 style={{ marginBottom: '20px' }}>📄 Markdown Preview</h2>
          <ReactMarkdown remarkPlugins={[remarkGfm]}>
            {previewContent}
          </ReactMarkdown>
        </div>
      )}
    </div>
  );
}

export default App;

