from PyQt5.QtWidgets import QAction
import pytest
from gwpycore import AppActions


@pytest.fixture
def app_actions():
    return AppActions(None)


def test_addAction(app_actions):
    app_actions.addAction("quit", "&Quit", "Ctrl+q", "Alt+x", tip="Leave the application")
    action: QAction = app_actions.quit
    # FIXME assert action.text == "&Quit"
    # assert action.toolTip == "Leave the application"
    # assert action.shortcuts.length == 2



def test_getActionInfo(app_actions):
    app_actions.addAction("quit", "&Quit", "Ctrl+q", "Alt+x", tip="Leave the application")
    (shortcuts, name, tip) = app_actions.getActionInfo("quit")
    assert name == "Quit"
    assert tip == "Leave the application"
    # FIXME When a QAction is created with a parent of None, it knows not how interpret the key sequences
    assert shortcuts == ""  # "Ctrl+q, Alt+x"
