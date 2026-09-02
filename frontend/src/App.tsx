import React, { useState, useEffect } from 'react';
import { LessonSidebar } from './components/LessonSidebar';
import { LessonDocumentationView } from './components/LessonDocumentationView';
import { EditDocumentationModal } from './components/EditDocumentationModal';
import { AddLessonModal } from './components/AddLessonModal';
import { MaterialPreviewModal } from './components/MaterialPreviewModal';
import { AddMaterialModal } from './components/AddMaterialModal';
import { Lesson, LessonStatus, LessonMaterial } from './types';
import { Group, GroupFormData } from './types/group';
import { GroupSelectModal } from './components/GroupSelectModal';
import { GroupDashboardView } from './components/GroupDashboardView';
import { Quiz } from './types/quiz';
import { AIQuizGeneratorModal } from './components/quiz/AIQuizGeneratorModal';
import { QuizEditorModal } from './components/quiz/QuizEditorModal';
import { QuizHostView } from './components/quiz/QuizHostView';
import { QuizPlayerView } from './components/quiz/QuizPlayerView';
import { QuizStandalonePortal } from './components/quiz/QuizStandalonePortal';
import { Menu, X, Sun, Moon, BookOpen, Loader2 } from 'lucide-react';
import { LoginView } from './components/LoginView';
import { ImportLessonsModal } from './components/ImportLessonsModal';
import { NotionSettingsView } from './components/NotionSettingsView';
import { NotionSyncModal } from './components/NotionSyncModal';
import { NotionSettings } from './notion/notionTypes';
import { PublicSharedLessonView } from './components/PublicSharedLessonView';

export default function App() {
  const isGameSubdomain = typeof window !== 'undefined' && (
    window.location.hostname.startsWith('game.') ||
    window.location.pathname === '/game' ||
    window.location.pathname.startsWith('/create') ||
    window.location.search.includes('app=game') ||
    window.location.search.includes('mode=create')
  );

  useEffect(() => {
    document.title = 'marimovdev';
  }, []);

  const [lessons, setLessons] = useState<Lesson[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [selectedLessonId, setSelectedLessonId] = useState<string>('');
  const [isLoggedIn, setIsLoggedIn] = useState<boolean>(() => localStorage.getItem('dars_rejasi_logged_in') === 'true');

  const [isDarkMode, setIsDarkMode] = useState<boolean>(false);
  const [isMobileSidebarOpen, setIsMobileSidebarOpen] = useState<boolean>(false);

  // Standalone Public Share state
  const [sharedLessonId, setSharedLessonId] = useState<string | null>(() => {
    const params = new URLSearchParams(window.location.search);
    const shareParam = params.get('share');
    if (shareParam) return shareParam;

    const path = window.location.pathname;
    if (path.startsWith('/share/')) {
      return path.replace('/share/', '');
    }
    return null;
  });

  // Group state
  const [groups, setGroups] = useState<Group[]>([]);
  const [activeGroupId, setActiveGroupId] = useState<string | null>(() => localStorage.getItem('dars_rejasi_active_group_id'));
  const [isGroupSelectModalOpen, setIsGroupSelectModalOpen] = useState<boolean>(false);

  // Quiz state
  const [activeQuiz, setActiveQuiz] = useState<Quiz | null>(null);
  const [isAIQuizModalOpen, setIsAIQuizModalOpen] = useState<boolean>(false);
  const [isQuizEditorModalOpen, setIsQuizEditorModalOpen] = useState<boolean>(false);

  // Modals & Navigation state
  const [isEditModalOpen, setIsEditModalOpen] = useState<boolean>(false);
  const [editingLesson, setEditingLesson] = useState<Lesson | null>(null);
  const [isAddLessonModalOpen, setIsAddLessonModalOpen] = useState<boolean>(false);
  const [isImportModalOpen, setIsImportModalOpen] = useState<boolean>(false);
  const [isSyncModalOpen, setIsSyncModalOpen] = useState<boolean>(false);
  const [currentView, setCurrentView] = useState<'lessons' | 'settings' | 'groups_dashboard' | 'quiz_host' | 'quiz_player'>('lessons');
  const [notionSettings, setNotionSettings] = useState<NotionSettings | null>(null);
  const [previewMaterial, setPreviewMaterial] = useState<LessonMaterial | null>(null);
  const [addMaterialLessonId, setAddMaterialLessonId] = useState<string | null>(null);

  const fetchNotionStatus = () => {
    fetch('/api/notion/status?t=' + Date.now())
      .then(res => res.json())
      .then(setNotionSettings)
      .catch(err => console.error("Error loading Notion status:", err));
  };

  const fetchGroups = async () => {
    try {
      const res = await fetch('/api/groups?t=' + Date.now());
      if (!res.ok) throw new Error("Failed to fetch groups");
      const data: Group[] = await res.json();
      setGroups(data);

      if (data.length > 0) {
        const savedId = localStorage.getItem('dars_rejasi_active_group_id');
        const found = data.find(g => g.id === savedId);
        if (found) {
          setActiveGroupId(found.id);
        } else {
          setActiveGroupId(data[0].id);
          localStorage.setItem('dars_rejasi_active_group_id', data[0].id);
        }
      } else {
        if (isLoggedIn) {
          setIsGroupSelectModalOpen(true);
        }
      }
    } catch (err) {
      console.warn("Failed to load groups:", err);
    }
  };

  const fetchGroupLessons = async (groupId: string) => {
    setLoading(true);
    try {
      const res = await fetch(`/api/groups/${groupId}/lessons?t=` + Date.now());
      if (!res.ok) throw new Error("Failed to fetch group lessons");
      const data: Lesson[] = await res.json();
      if (Array.isArray(data) && data.length > 0) {
        setLessons(data);
        localStorage.setItem('dars_rejasi_lessons', JSON.stringify(data));
        
        const currentLessonObj = data.find(l => l.status === 'current') || data[0];
        setSelectedLessonId(currentLessonObj.id);
      }
    } catch (err) {
      console.error("Error loading group lessons:", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchNotionStatus();
    if (isLoggedIn) {
      fetchGroups();
    }
  }, [isLoggedIn]);

  useEffect(() => {
    if (activeGroupId) {
      fetchGroupLessons(activeGroupId);
    } else {
      fetch('/api/lessons?t=' + Date.now())
        .then(res => res.json())
        .then((data: Lesson[]) => {
          if (Array.isArray(data) && data.length > 0) {
            setLessons(data);
            setSelectedLessonId(data[0].id);
          }
          setLoading(false);
        })
        .catch(() => setLoading(false));
    }
  }, [activeGroupId]);
  useEffect(() => {
    const savedTheme = localStorage.getItem('marimov_dark_mode');
    if (savedTheme === 'true' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      setIsDarkMode(true);
      document.documentElement.classList.add('dark');
    } else {
      setIsDarkMode(false);
      document.documentElement.classList.remove('dark');
    }
  }, []);

  const handleToggleDarkMode = () => {
    setIsDarkMode(prev => {
      const next = !prev;
      localStorage.setItem('marimov_dark_mode', String(next));
      if (next) {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
      return next;
    });
  };

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const lessonParam = params.get('lesson');
    if (lessonParam && lessons.length > 0) {
      const found = lessons.find(l => l.id === lessonParam || l.lessonNumber.toString() === lessonParam);
      if (found) {
        setSelectedLessonId(found.id);
      }
    }
  }, [lessons]);

  const activeGroup = groups.find(g => g.id === activeGroupId) || null;
  const selectedLesson = lessons.find(l => l.id === selectedLessonId) || lessons[0];

  const handleSelectGroup = (groupId: string) => {
    setActiveGroupId(groupId);
    localStorage.setItem('dars_rejasi_active_group_id', groupId);
    setCurrentView('lessons');
  };

  const handleCreateGroup = async (formData: GroupFormData) => {
    const res = await fetch('/api/groups', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData)
    });
    if (!res.ok) {
      const errData = await res.json();
      throw new Error(errData.error || "Guruh yaratishda xatolik yuz berdi");
    }
    const newGroup: Group = await res.json();
    await fetchGroups();
    handleSelectGroup(newGroup.id);
  };

  const handleDeleteGroup = async (groupId: string) => {
    try {
      await fetch(`/api/groups/${groupId}`, { method: 'DELETE' });
      const nextGroups = groups.filter(g => g.id !== groupId);
      setGroups(nextGroups);
      if (activeGroupId === groupId) {
        if (nextGroups.length > 0) {
          handleSelectGroup(nextGroups[0].id);
        } else {
          setActiveGroupId(null);
          localStorage.removeItem('dars_rejasi_active_group_id');
          setIsGroupSelectModalOpen(true);
        }
      }
    } catch (err) {
      console.error("Failed to delete group:", err);
    }
  };

  const saveLessonsLocally = (nextLessons: Lesson[]) => {
    setLessons(nextLessons);
    localStorage.setItem('dars_rejasi_lessons', JSON.stringify(nextLessons));
  };

  const handleUpdateStatus = (lessonId: string, status: LessonStatus) => {
    const next = lessons.map(l => l.id === lessonId ? { ...l, status } : l);
    saveLessonsLocally(next);

    if (activeGroupId) {
      fetch(`/api/groups/${activeGroupId}/lessons/${lessonId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status })
      })
      .then(() => fetchGroups())
      .catch(err => console.warn("Group status sync failed:", err));
    } else {
      fetch(`/api/lessons/${lessonId}/status`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status })
      }).catch(err => console.warn("Backend status sync failed:", err));
    }
  };

  const handleBatchUpdateStatus = async (lessonIds: string[], status: LessonStatus) => {
    const next = lessons.map(l => lessonIds.includes(l.id) || lessonIds.includes(l.lessonNumber.toString()) ? { ...l, status } : l);
    saveLessonsLocally(next);

    try {
      if (activeGroupId) {
        await fetch(`/api/groups/${activeGroupId}/lessons/batch-status`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ lessonIds, status })
        });
        fetchGroups();
      } else {
        await fetch(`/api/lessons/batch-status`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ lessonIds, status })
        });
      }
    } catch (err) {
      console.warn("Batch status update error:", err);
    }
  };

  const handleOpenEdit = (lesson: Lesson) => {
    setEditingLesson(lesson);
    setIsEditModalOpen(true);
  };

  const handleSaveDocumentation = (updatedLesson: Lesson) => {
    const next = lessons.map(l => l.id === updatedLesson.id ? updatedLesson : l);
    saveLessonsLocally(next);

    if (activeGroupId) {
      fetch(`/api/groups/${activeGroupId}/lessons/${updatedLesson.id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          notes: updatedLesson.homework,
          status: updatedLesson.status
        })
      }).catch(err => console.warn("Group lesson update failed:", err));
    }

    fetch(`/api/lessons/${updatedLesson.id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(updatedLesson)
    }).catch(err => console.warn("Backend documentation sync failed:", err));
  };

  const handleAddLesson = (newLesson: Lesson) => {
    const next = [...lessons, newLesson];
    saveLessonsLocally(next);
    setSelectedLessonId(newLesson.id);

    fetch('/api/lessons', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newLesson)
    }).catch(err => console.warn("Backend add lesson sync failed:", err));
  };

  const handleDeleteLesson = (lessonId: string) => {
    const nextLessons = lessons.filter(l => l.id !== lessonId);
    saveLessonsLocally(nextLessons);
    if (selectedLessonId === lessonId) {
      setSelectedLessonId(nextLessons.length > 0 ? nextLessons[0].id : '');
    }

    fetch(`/api/lessons/${lessonId}`, { method: 'DELETE' })
      .catch(err => console.warn("Backend delete sync failed:", err));
  };

  const handleAddMaterial = (material: LessonMaterial) => {
    if (!addMaterialLessonId) return;
    const lessonObj = lessons.find(l => l.id === addMaterialLessonId);
    if (!lessonObj) return;
    const updatedLesson = {
      ...lessonObj,
      materials: [...(lessonObj.materials || []), material]
    };
    handleSaveDocumentation(updatedLesson);
    setAddMaterialLessonId(null);
  };

  const handleImportLessons = (importedLessons: Lesson[], overwrite: boolean) => {
    let nextLessons: Lesson[];
    if (overwrite) {
      nextLessons = importedLessons;
    } else {
      const maxLessonNum = lessons.length > 0 ? Math.max(...lessons.map(l => l.lessonNumber)) : 0;
      const adjustedImported = importedLessons.map((l, i) => ({
        ...l,
        lessonNumber: maxLessonNum + i + 1,
        id: `les-imported-${maxLessonNum + i + 1}-${Date.now()}`
      }));
      nextLessons = [...lessons, ...adjustedImported];
    }
    
    saveLessonsLocally(nextLessons);
    if (nextLessons.length > 0) {
      setSelectedLessonId(nextLessons[0].id);
    }
  };

  const handleSyncComplete = () => {
    localStorage.removeItem('dars_rejasi_lessons');
    if (activeGroupId) {
      fetchGroupLessons(activeGroupId);
    }
    fetchNotionStatus();
  };

  const handleLogout = () => {
    localStorage.removeItem('dars_rejasi_logged_in');
    localStorage.removeItem('dars_rejasi_active_group_id');
    setIsLoggedIn(false);
    setActiveGroupId(null);
  };

  const toggleDarkMode = () => {
    setIsDarkMode(prev => {
      const next = !prev;
      if (next) {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
      return next;
    });
  };

  if (sharedLessonId) {
    return (
      <PublicSharedLessonView
        lessonId={sharedLessonId}
        onBackToApp={() => {
          setSharedLessonId(null);
          window.history.pushState({}, '', '/');
        }}
      />
    );
  }

  if (isGameSubdomain) {
    return <QuizStandalonePortal lessons={lessons} />;
  }

  if (!isLoggedIn) {
    return <LoginView onLogin={() => setIsLoggedIn(true)} />;
  }

  // Full Screen Quiz Host View
  if (currentView === 'quiz_host' && activeQuiz) {
    return <QuizHostView quiz={activeQuiz} onExit={() => setCurrentView('lessons')} />;
  }

  // Full Screen Quiz Player View
  if (currentView === 'quiz_player') {
    return <QuizPlayerView onExit={() => setCurrentView('lessons')} />;
  }

  if (loading && lessons.length === 0) {
    return (
      <div className="min-h-screen flex flex-col items-center justify-center bg-slate-50 dark:bg-slate-950 text-slate-500">
        <Loader2 className="w-10 h-10 text-blue-600 animate-spin mb-3" />
        <span className="text-xs font-semibold">Guruh dars rejalari yuklanmoqda...</span>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 flex flex-col md:flex-row font-sans antialiased overflow-x-hidden">
      
      {/* Mobile Top Header */}
      <div className="md:hidden flex items-center justify-between p-4 bg-white dark:bg-slate-900 border-b border-slate-200 dark:border-slate-800 sticky top-0 z-30">
        <button
          onClick={() => setIsMobileSidebarOpen(!isMobileSidebarOpen)}
          className="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300"
        >
          {isMobileSidebarOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
        </button>

        <div className="flex items-center gap-2">
          <button
            onClick={() => setIsGroupSelectModalOpen(true)}
            className="px-3 py-1 bg-blue-50 dark:bg-blue-950 text-blue-600 dark:text-blue-400 rounded-lg font-bold text-xs"
          >
            {activeGroup ? activeGroup.name : 'Guruh tanlash'}
          </button>
        </div>

        <button
          onClick={handleToggleDarkMode}
          className="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-amber-500 dark:text-yellow-400 cursor-pointer"
        >
          {isDarkMode ? <Sun className="w-5 h-5" /> : <Moon className="w-5 h-5 text-purple-600" />}
        </button>
      </div>

      {/* Sidebar for Desktop & Mobile */}
      <div className={`fixed md:relative z-40 inset-y-0 left-0 transform ${
        isMobileSidebarOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0'
      } transition-transform duration-300 ease-in-out`}>
        <LessonSidebar
          lessons={lessons}
          selectedLessonId={selectedLessonId}
          onSelectLesson={(id) => {
            setSelectedLessonId(id);
            setIsMobileSidebarOpen(false);
            setCurrentView('lessons');
          }}
          onOpenAddModal={() => setIsAddLessonModalOpen(true)}
          onOpenImportModal={() => setIsImportModalOpen(true)}
          onOpenSettings={() => setCurrentView('settings')}
          onLogout={handleLogout}
          groups={groups}
          activeGroup={activeGroup}
          onOpenGroupSelectModal={() => setIsGroupSelectModalOpen(true)}
          onOpenGroupDashboard={() => setCurrentView('groups_dashboard')}
          onOpenAIQuizGenerator={() => setIsAIQuizModalOpen(true)}
          onOpenPlayerView={() => setCurrentView('quiz_player')}
          onBatchUpdateStatus={handleBatchUpdateStatus}
          isDarkMode={isDarkMode}
          onToggleDarkMode={handleToggleDarkMode}
        />
      </div>

      {/* Backdrop for Mobile Sidebar */}
      {isMobileSidebarOpen && (
        <div 
          onClick={() => setIsMobileSidebarOpen(false)}
          className="fixed inset-0 bg-slate-900/50 backdrop-blur-xs z-30 md:hidden"
        />
      )}

      {/* Main Content Workspace */}
      <main className="flex-1 flex flex-col min-w-0 h-screen overflow-y-auto">
        {currentView === 'settings' ? (
          <NotionSettingsView
            settings={notionSettings}
            onBackToLessons={() => setCurrentView('lessons')}
            onOpenSyncModal={() => setIsSyncModalOpen(true)}
          />
        ) : currentView === 'groups_dashboard' ? (
          <GroupDashboardView
            groups={groups}
            activeGroupId={activeGroupId}
            onSelectGroup={handleSelectGroup}
            onOpenCreateModal={() => setIsGroupSelectModalOpen(true)}
            onDeleteGroup={handleDeleteGroup}
          />
        ) : selectedLesson ? (
          <LessonDocumentationView
            lesson={selectedLesson}
            onUpdateStatus={handleUpdateStatus}
            onOpenEdit={() => handleOpenEdit(selectedLesson)}
            onDeleteLesson={() => handleDeleteLesson(selectedLesson.id)}
            onPreviewMaterial={(material) => setPreviewMaterial(material)}
            onAddMaterialClick={() => setAddMaterialLessonId(selectedLesson.id)}
          />
        ) : (
          <div className="flex-1 flex flex-col items-center justify-center p-8 text-center text-slate-400">
            <BookOpen className="w-16 h-16 mb-4 text-slate-300 dark:text-slate-700" />
            <h3 className="text-lg font-bold text-slate-700 dark:text-slate-300">Dars tanlanmagan</h3>
            <p className="text-xs text-slate-500 mt-1 max-w-sm">
              Yon paneldan biror darsni tanlang yoki yangi dars/guruh qo'shing.
            </p>
          </div>
        )}
      </main>

      {/* AI Quiz Generator Modal */}
      <AIQuizGeneratorModal
        isOpen={isAIQuizModalOpen}
        onClose={() => setIsAIQuizModalOpen(false)}
        lessons={lessons}
        onQuizGenerated={(generatedQuiz) => {
          setActiveQuiz(generatedQuiz);
          setIsQuizEditorModalOpen(true);
        }}
      />

      {/* Quiz Editor Modal */}
      {activeQuiz && (
        <QuizEditorModal
          isOpen={isQuizEditorModalOpen}
          onClose={() => setIsQuizEditorModalOpen(false)}
          quiz={activeQuiz}
          onStartLiveSession={(finalQuiz) => {
            setActiveQuiz(finalQuiz);
            setCurrentView('quiz_host');
          }}
        />
      )}

      {/* Group Selection / Creation Modal */}
      <GroupSelectModal
        isOpen={isGroupSelectModalOpen}
        onClose={() => setIsGroupSelectModalOpen(false)}
        groups={groups}
        activeGroupId={activeGroupId}
        onSelectGroup={handleSelectGroup}
        onCreateGroup={handleCreateGroup}
      />

      {/* Edit Documentation Modal */}
      {editingLesson && (
        <EditDocumentationModal
          isOpen={isEditModalOpen}
          onClose={() => {
            setIsEditModalOpen(false);
            setEditingLesson(null);
          }}
          lesson={editingLesson}
          onSave={handleSaveDocumentation}
        />
      )}

      {/* Add Lesson Modal */}
      <AddLessonModal
        isOpen={isAddLessonModalOpen}
        onClose={() => setIsAddLessonModalOpen(false)}
        onAddLesson={handleAddLesson}
        nextLessonNumber={lessons.length > 0 ? Math.max(...lessons.map(l => l.lessonNumber)) + 1 : 1}
      />

      {/* Material Preview Modal */}
      <MaterialPreviewModal
        isOpen={!!previewMaterial}
        onClose={() => setPreviewMaterial(null)}
        material={previewMaterial}
      />

      {/* Add Material Modal */}
      <AddMaterialModal
        isOpen={!!addMaterialLessonId}
        onClose={() => setAddMaterialLessonId(null)}
        onAddMaterial={handleAddMaterial}
      />

      {/* Import Lessons Modal */}
      <ImportLessonsModal
        isOpen={isImportModalOpen}
        onClose={() => setIsImportModalOpen(false)}
        onImport={handleImportLessons}
      />

      {/* Notion Sync Modal */}
      <NotionSyncModal
        isOpen={isSyncModalOpen}
        onClose={() => setIsSyncModalOpen(false)}
        settings={notionSettings}
        onSyncComplete={handleSyncComplete}
      />
    </div>
  );
}
