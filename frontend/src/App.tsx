import { useState } from 'react';
import axios from 'axios';
import { Upload, Loader2, CheckCircle, XCircle, Download } from 'lucide-react';

const API_URL = 'http://localhost:8000';
const API_KEY = 'test-key-123';

interface JobResponse {
  job_id: string;
  status: string;
  message: string;
  check_status: string;
}

interface StatusResponse {
  job_id: string;
  status: string;
  original_filename: string;
  original_size: number;
  processed_size?: number;
  download_url?: string;
  error_message?: string;
}

function App() {
  const [file, setFile] = useState<File | null>(null);
  const [uploading, setUploading] = useState(false);
  const [jobId, setJobId] = useState<string | null>(null);
  const [status, setStatus] = useState<StatusResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [checking, setChecking] = useState(false);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
      setError(null);
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setError('Lütfen bir dosya seçin');
      return;
    }

    setUploading(true);
    setError(null);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post<JobResponse>(
        `${API_URL}/api/v1/upload`,
        formData,
        {
          headers: {
            'X-API-Key': API_KEY,
            'Content-Type': 'multipart/form-data',
          },
        }
      );

      setJobId(response.data.job_id);
      setStatus(null);
      
      // Status'u kontrol etmeye başla
      checkStatus(response.data.job_id);
      
    } catch (err: unknown) {
      const error = err as { response?: { data?: { detail?: string } } };
      setError(error.response?.data?.detail || 'Upload başarısız');
    } finally {
      setUploading(false);
    }
  };

  const checkStatus = async (id: string) => {
    setChecking(true);
    try {
      const response = await axios.get<StatusResponse>(
        `${API_URL}/api/v1/status/${id}`
      );
      setStatus(response.data);

      if (response.data.status === 'completed' || response.data.status === 'failed') {
        setChecking(false);
        return;
      }

      // 2 saniye sonra tekrar kontrol et
      setTimeout(() => checkStatus(id), 2000);
    } catch {
      setError('Status kontrolü başarısız');
      setChecking(false);
    }
  };

  const handleDownload = () => {
    if (status?.download_url) {
      window.open(`http://localhost:8000${status.download_url}`, '_blank');
    }
  };

  const handleReset = () => {
    setFile(null);
    setJobId(null);
    setStatus(null);
    setError(null);
    setUploading(false);
    setChecking(false);
  };

  const getStatusIcon = () => {
    if (!status) return null;
    switch (status.status) {
      case 'pending':
      case 'queued':
        return <Loader2 className="w-8 h-8 text-yellow-500 animate-spin" />;
      case 'processing':
        return <Loader2 className="w-8 h-8 text-blue-500 animate-spin" />;
      case 'completed':
        return <CheckCircle className="w-8 h-8 text-green-500" />;
      case 'failed':
        return <XCircle className="w-8 h-8 text-red-500" />;
      default:
        return null;
    }
  };

  const getStatusText = () => {
    if (!status) return '';
    const map: Record<string, string> = {
      pending: '⏳ Beklemede',
      queued: '📤 Sıraya alındı',
      processing: '🔄 İşleniyor...',
      completed: '✅ Tamamlandı!',
      failed: '❌ Başarısız',
    };
    return map[status.status] || status.status;
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 flex items-center justify-center p-4">
      <div className="w-full max-w-2xl bg-white/10 backdrop-blur-lg rounded-3xl p-8 shadow-2xl border border-white/20">
        
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-white mb-2">
            🖼️ Image Sanitizer
          </h1>
          <p className="text-gray-300">
            Fotoğraflarından metadata temizle, optimize et ve indir
          </p>
        </div>

        {/* Upload Area */}
        <div className="border-2 border-dashed border-white/30 rounded-2xl p-8 mb-6 hover:border-purple-400 transition-colors">
          <input
            type="file"
            id="file-upload"
            accept="image/*"
            onChange={handleFileChange}
            className="hidden"
          />
          <label
            htmlFor="file-upload"
            className="cursor-pointer flex flex-col items-center justify-center gap-4"
          >
            <Upload className="w-16 h-16 text-purple-400" />
            <div className="text-white text-center">
              {file ? (
                <p className="text-lg font-semibold text-purple-300">{file.name}</p>
              ) : (
                <>
                  <p className="text-lg font-semibold">Fotoğraf seç</p>
                  <p className="text-sm text-gray-400">veya sürükle bırak</p>
                </>
              )}
            </div>
          </label>
        </div>

        {/* Buttons */}
        <div className="flex gap-4 mb-6">
          <button
            onClick={handleUpload}
            disabled={!file || uploading}
            className="flex-1 bg-gradient-to-r from-purple-500 to-pink-500 text-white font-bold py-3 px-6 rounded-xl hover:opacity-90 transition disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {uploading ? (
              <span className="flex items-center justify-center gap-2">
                <Loader2 className="w-5 h-5 animate-spin" />
                Yükleniyor...
              </span>
            ) : (
              '🚀 Yükle ve İşle'
            )}
          </button>
          <button
            onClick={handleReset}
            className="bg-white/10 text-white font-bold py-3 px-6 rounded-xl hover:bg-white/20 transition"
          >
            Temizle
          </button>
        </div>

        {/* Error */}
        {error && (
          <div className="bg-red-500/20 border border-red-500/50 text-red-200 p-4 rounded-xl mb-6">
            ❌ {error}
          </div>
        )}

        {/* Status */}
        {jobId && status && (
          <div className="bg-white/5 rounded-2xl p-6 border border-white/10">
            <div className="flex items-center gap-4 mb-4">
              {getStatusIcon()}
              <div>
                <p className="text-white font-semibold">{getStatusText()}</p>
                <p className="text-gray-400 text-sm">ID: {jobId.substring(0, 12)}...</p>
              </div>
            </div>

            {status.status === 'completed' && (
              <>
                <div className="grid grid-cols-2 gap-4 mb-4 text-sm">
                  <div>
                    <p className="text-gray-400">Orijinal</p>
                    <p className="text-white font-semibold">
                      {(status.original_size / 1024).toFixed(1)} KB
                    </p>
                  </div>
                  <div>
                    <p className="text-gray-400">İşlenmiş</p>
                    <p className="text-white font-semibold">
                      {status.processed_size ? (status.processed_size / 1024).toFixed(1) : '0'} KB
                    </p>
                  </div>
                </div>
                <button
                  onClick={handleDownload}
                  className="w-full bg-gradient-to-r from-green-500 to-emerald-500 text-white font-bold py-3 px-6 rounded-xl hover:opacity-90 transition flex items-center justify-center gap-2"
                >
                  <Download className="w-5 h-5" />
                  İndir (WEBP)
                </button>
              </>
            )}

            {checking && status.status !== 'completed' && status.status !== 'failed' && (
              <div className="mt-4 flex items-center justify-center gap-2 text-gray-400">
                <Loader2 className="w-4 h-4 animate-spin" />
                <span className="text-sm">İşlem devam ediyor...</span>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;